<template>
  <div ref="refSlide" class="main">
    <div v-for="item, index in state.chatList" :key="item">
      <div :class="[item.who == 'ai' ? 'date-left' : 'date-right']">{{ item.date }}</div>
      <div :class="[item.who == 'ai' ? 'chat-left' : 'chat-right']">
        <span v-if="storeChat.ifLoadingAI">
          <!-- loading -->
          <SvgIcon v-if="index + 1 == state.chatList.length" name="ele-Loading" :size="10" class="is-loading" color="#337ecc"></SvgIcon>
          {{ item.content }}
        </span>
        <MsgTextarea v-else :text="item.content" />
      </div>
    </div>
  </div>
</template>

<script setup>
import MsgTextarea from '@/components/Main/MsgTextarea.vue'
import { ElLoading } from 'element-plus'
import { getCurrentInstance, ref, reactive, watch, onMounted, onUnmounted, nextTick } from 'vue'
import { useStoreAside } from '@/stores/aside'
import { useStoreChat } from '@/stores/chat'

const storeAside = useStoreAside()
const storeChat = useStoreChat()
const cxt = getCurrentInstance()
const bus = cxt.appContext.config.globalProperties.$bus
const refSlide = ref(null)
const state = reactive({
  chatList: [],
  timer: '',
  timer2: '',
  showCountdown: 300,
  loading: ''
})

onMounted(() => {
  state.timer = setInterval(() => {
    if (window.pywebview != undefined) {
      getChatContentList(storeAside.selectTitle)
      clearInterval(state.timer)
      state.timer = ''
    }
  }, 100)

  bus.on('busSetNewQ', (newQ) => {
    newQ = newQ.trim()
    if (newQ != '') {
      getNewQ(newQ)
    }
  })
})

onUnmounted(() => {
  clearInterval(state.timer)
  state.timer = ''
  closeLoading()
  bus.off('busSetNewQ')
})

const clear = () => {
  state.chatList = []
}

const slideToBottom = () => {
  // 滑动到底
  nextTick(() => {
    refSlide.value.scrollTo({
      top: refSlide.value.scrollHeight,
      //滚动过渡效果
      behavior: "smooth"
    });
  })
}

const getNewQ = (newQ) => {
  let nowTime = new Date()
  nowTime = nowTime.toLocaleString()
  nowTime = nowTime.replaceAll('/', '-')
  state.chatList.push({ 'who': 'my', 'content': newQ, 'date': nowTime })
  state.chatList.push({ 'who': 'ai', 'content': '...', 'date': nowTime })
  window.pywebview.api.chat_addContent(storeAside.selectTitle, 'my', newQ)
  slideToBottom() // 滑动到底

  // 显示倒计时
  showLoading()

  // openIA
  window.pywebview.api.chat_getAI(storeAside.selectTitle, newQ).then((res) => {
    // console.log('res', res)
    closeLoading()
    let nowTime = new Date()
    nowTime = nowTime.toLocaleString()
    nowTime = nowTime.replaceAll('/', '-')
    state.chatList.splice(state.chatList.length - 1, 1, { 'who': 'ai', 'content': res, 'date': nowTime })
    window.pywebview.api.chat_addContent(storeAside.selectTitle, 'ai', res)
    slideToBottom() // 滑动到底
  })
}

const getChatContentList = (title) => {
  state.chatList = []
  window.pywebview.api.chat_getContentList(title, 1, 200).then((res) => {
    for (const item of res.list) {
      state.chatList.push({ 'who': item['who'], 'content': item['content'], 'date': item['updated_at'] })
    }
    slideToBottom() // 滑动到底
  })
}

// 显示倒计时
const showLoading = () => {
  state.loading = ElLoading.service({
    lock: true,
    body: true,
    text: '',
    spinner: 'sunny',
    background: 'rgba(0, 0, 0, 0.1)',
  })
  state.showCountdown = 300
  storeChat.setIfLoadingAI(true)
  let nowTime = new Date()
  nowTime = nowTime.toLocaleString()
  nowTime = nowTime.replaceAll('/', '-')
  state.chatList.splice(state.chatList.length - 1, 1, { 'who': 'ai', 'content': String(state.showCountdown) + '秒...', 'date': nowTime })
  state.timer2 = setInterval(() => {
    let nowTime = new Date()
    nowTime = nowTime.toLocaleString()
    nowTime = nowTime.replaceAll('/', '-')
    state.showCountdown -= 1
    if (state.timer2 != '') {
      if (state.showCountdown <= 0) {
        state.chatList.splice(state.chatList.length - 1, 1, { 'who': 'ai', 'content': '访问超时', 'date': nowTime })
        closeLoading()
      } else {
        state.chatList.splice(state.chatList.length - 1, 1, { 'who': 'ai', 'content': String(state.showCountdown) + '秒...', 'date': nowTime })
      }
    }
  }, 1000)
}
const closeLoading = () => {
  clearInterval(state.timer2)
  state.timer2 = ''
  storeChat.setIfLoadingAI(false)
  state.loading.close()
  slideToBottom() // 滑动到底
}

// watch(
//   () => storeChat.newQ,
//   (val) => {
//     console.log('watch-newQ1', val)
//     val = val.trim()
//     console.log('watch-newQ2', val)
//     if (val != '') {
//       console.log('watch-newQ3', val)
//       getNewQ(val)
//     }
//   },
//   { immediate: true }
// )

watch(
  () => storeAside.selectTitle,
  (val) => {
    getChatContentList(val)
  }
)

defineExpose({ clear })
</script>

<style scoped>
.main {
  height: calc(100vh - 200px);
  overflow: scroll;
  background-color: #F3F3F3;
}

.date-left {
  display: table;
  margin: 30px auto 4px 30px;
  color: #A8ABB2;
}

.date-right {
  display: table;
  max-width: calc(100% - 200px);
  margin: 30px 30px 4px auto;
  color: #A8ABB2;
}

.chat-left {
  display: table;
  max-width: calc(100% - 200px);
  width: fit-content;
  margin: 0px auto 30px 20px;
  padding: 10px;
  border-radius: 15px;
  background-color: white;
}

.chat-right {
  display: table;
  max-width: calc(100% - 200px);
  width: fit-content;
  margin: 0px 20px 30px auto;
  padding: 10px;
  border-radius: 15px;
  background-color: #4397F7;
  color: white;
}
</style>
