<template>
  <div class="display-row layout">
    <Aside />
    <div class="display w100 h100">
      <Header @onClear="onHeaderClear" />
      <Main ref="refMain" />
      <Footer />
    </div>

    <!-- 初次填写SK码 -->
    <CreateSK :visible="state.visibleCreateSK" />
  </div>
</template>

<script setup>
import CreateSK from '@/components/CreateSK/index.vue'
import Aside from '@/components/Aside/index.vue'
import Header from '@/components/Header/index.vue'
import Main from '@/components/Main/index.vue'
import Footer from '@/components/Footer/index.vue'

import { ref, reactive, onMounted, onUnmounted } from 'vue'
import { useStoreAside } from '@/stores/aside'

const storeAside = useStoreAside()

const refMain = ref(null)
const state = reactive({
  timer: '',
  visibleCreateSK: false
})

onMounted(() => {
  // 初始化
  state.timer = setInterval(() => {
    if (window.pywebview != undefined) {
      getAppInfo() // 程序基础配置信息
      getItemList() // 获取聊天类别列表
      getSkOpenAI() // 获取 OpenAI 的sk码
      clearInterval(state.timer)
      state.timer = ''
    }
  }, 100)
})

onUnmounted(() => {
  clearInterval(state.timer)
  state.timer = ''
})

// 清空消息
const onHeaderClear = () => {
  refMain.value.clear()
}

// 获取 OpenAI 的sk码
const getSkOpenAI = () => {
  window.pywebview.api.chat_getSkOpenAI().then((skOpenAI) => {
    // console.log('setSkOpenAI', skOpenAI)
    if (skOpenAI == '') {
      // 弹出对话框 输入openAI的sk码
      state.visibleCreateSK = true
    } else {
      // 设置全局sk码
      window.pywebview.api.chat_setSkOpenAI(skOpenAI)
    }
  })
}

// 获取聊天类别列表
const getItemList = () => {
  window.pywebview.api.chat_getTitleList().then((res) => {
    // console.log('getItemList', res)
    storeAside.setChatTitleInfoList(res)
    storeAside.setSelectTitle(res[0]['title'])
  })
}

// 程序基础配置信息
const getAppInfo = () => {
  window.pywebview.api.system_getAppInfo().then((res) => {
    storeAside.setAppInfo(res)
  })
}

</script>

<style scoped>
.main {
  height: calc(100vh - 200px);
}

.layout {
  height: 100vh;
}
</style>
