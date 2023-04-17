<template>
  <div class="footer center-c">
    <el-input v-model="state.inputStr" type="textarea" placeholder="请在此输入..." />
  </div>
</template>

<script setup>
import { ElMessage } from 'element-plus'
import { getCurrentInstance, reactive, onMounted } from 'vue'
import { useStoreChat } from '@/stores/chat'

const storeChat = useStoreChat()
const cxt = getCurrentInstance()
const bus = cxt.appContext.config.globalProperties.$bus
const state = reactive({
  inputStr: '',
  questions: ''
})


onMounted(() => {
  document.onkeydown = function (e) {
    if (e.key === 'Enter') {
      let questions = state.inputStr.trim()
      if (questions != '') {
        if (storeChat.ifLoadingAI) {
          ElMessage({ type: 'warning', message: '请等待回复后，再给出新的对话', grouping: true })
          state.inputStr = questions
        } else {
          storeChat.setNewQ(questions)
          bus.emit('busSetNewQ', questions)
          state.inputStr = ''
        }
      } else {
        state.inputStr = questions
      }
    }
  }
})

// 清空输入框
const clear = () => {
  state.inputStr = ''
}

defineExpose({ clear })
</script>

<style scoped>
.footer {
  height: 140px;
}

:deep(.el-input) {
  height: 140px;
  border-radius: 0px;
}

:deep(.el-textarea__inner) {
  height: 140px;
  background: #F3F3F3;
  border-radius: 0px;
  font-size: 14px;
  font-weight: 400;
  color: #2c2c2c;
  resize: none;
}
</style>
