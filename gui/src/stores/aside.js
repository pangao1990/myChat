import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useStoreAside = defineStore('Aside', () => {
  // 程序基础配置信息
  const appInfo = ref({ appName: '', appVersion: '' })
  function setAppInfo(data) {
    appInfo.value = data
  }

  // 主题对话列表 [{'title': '', 'theme': '', 'model': '', 'temperature': '', 'news_count': ''}]
  const chatTitleInfoList = ref([])
  function addChatTitleInfoList(info) {
    chatTitleInfoList.value.push(info)
    console.log('info', info)
    window.pywebview.api.chat_addTitle(info.title, info.theme, info.model, info.temperature, info.news_count)
  }
  function setChatTitleInfoList(infoList) {
    chatTitleInfoList.value = infoList.map((item) => {
      // 修改时间 变化格式
      const updateDate = item['updated_at']
      if (updateDate == undefined) {
        item['date'] = ''
        item['time'] = ''
      } else {
        item['date'] = updateDate.slice(0, 10).replaceAll('-', '/')
        item['time'] = updateDate.slice(11, 16)
      }
      return item
    })
  }
  function getChatTitleInfo(title) {
    for (const chatTitleInfo of chatTitleInfoList.value) {
      if (chatTitleInfo.title == title) {
        return chatTitleInfo.info
      }
    }
    return {}
  }
  function deleteChatTitleList(title) {
    for (const index in chatTitleInfoList.value) {
      if (chatTitleInfoList.value[index]['title'] == title) {
        chatTitleInfoList.value.splice(index, 1)
        window.pywebview.api.chat_deleteTitle(title)
        break
      }
    }
  }
  function updateChatTitleList(title, info) {
    for (const index in chatTitleInfoList.value) {
      if (chatTitleInfoList.value[index]['title'] == title) {
        chatTitleInfoList.value.splice(index, 1, info)
        console.log(2, chatTitleInfoList.value)
        window.pywebview.api.chat_updateTitle(title, info)
        break
      }
    }
  }

  // 所选标题
  const selectTitle = ref('')
  const selectTitleInfo = ref({ title: '', theme: '', model: 'gpt-3.5-turbo', temperature: 1, news_count: 0, date: '', time: '' })
  function setSelectTitle(title) {
    selectTitle.value = title
    visibleThemeStore.value = false // 关闭主题广场
    for (const chatTitleInfo of chatTitleInfoList.value) {
      if (chatTitleInfo.title == title) {
        selectTitleInfo.value = chatTitleInfo
      }
    }
  }

  // 主题广场
  const visibleThemeStore = ref(false)
  function setVisibleThemeStore(visible) {
    visibleThemeStore.value = visible
  }

  return {
    appInfo,
    setAppInfo,
    chatTitleInfoList,
    addChatTitleInfoList,
    setChatTitleInfoList,
    getChatTitleInfo,
    deleteChatTitleList,
    updateChatTitleList,
    selectTitle,
    selectTitleInfo,
    setSelectTitle,
    visibleThemeStore,
    setVisibleThemeStore
  }
})
