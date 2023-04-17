import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useDark, useToggle } from '@vueuse/core'

export const useStoreTheme = defineStore('theme', () => {
  const themeConfigInit = {
    globalTitle: 'myChat', // 网站主标题（菜单导航、浏览器当前网页标题）

    // 主题色
    isDark: false,

    // 组件大小
    componentSize: 'small' // 默认全局组件大小，可选值"<large|default|small>"，默认 default
  }

  const themeConfig = ref(themeConfigInit)

  function setThemeConfig(data) {
    // 设置主题
    themeConfig.value = data
  }

  function reset() {
    // 重置主题
    themeConfig.value = themeConfigInit
  }

  function setDark() {
    // 设置暗黑模式
    toggleDark()
    themeConfig.value.isDark = isDark
  }

  return {
    themeConfig,
    setThemeConfig,
    reset,
    setDark
  }
})

// 暗黑模式
const isDark = useDark({
  storageKey: 'vueuse_isDark', // 存储到localStorage中的Key
  valueDark: 'dark', // 暗黑class名字
  valueLight: 'light' // 高亮class名字
})
const toggleDark = useToggle(isDark)
