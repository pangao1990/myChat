import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useStoreChat = defineStore('Chat', () => {
  // 对话内容列表
  const chatContentList = ref([])
  function setChatContentList(data) {
    console.log('data', data)
    chatContentList.value = data
  }
  function pushChatContentList(data) {
    chatContentList.value.push(data)
  }

  // 新的提问
  const newQ = ref('')
  function setNewQ(data) {
    newQ.value = data
  }

  // 是否连接AI中
  const ifLoadingAI = ref(false)
  function setIfLoadingAI(bool) {
    ifLoadingAI.value = bool
  }

  return {
    chatContentList,
    setChatContentList,
    pushChatContentList,
    newQ,
    setNewQ,
    ifLoadingAI,
    setIfLoadingAI
  }
})
