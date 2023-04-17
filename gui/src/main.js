import { createApp } from 'vue'

import App from '@/App.vue'

const app = createApp(App)

// 状态管理 pinia
import pinia from '@/stores'
app.use(pinia)

// 事件总线
import mitt from 'mitt'
app.config.globalProperties.$bus = mitt()

// 组件库 ElementPlus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/dark/css-vars.css' // 暗黑模式
app.use(ElementPlus)

// 图标库 ElementPlus
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(`ele-${key}`, component)
}
// 自定义图标库
import SvgIcon from '@/components/SvgIcon/index.vue'
app.component('SvgIcon', SvgIcon)

// 代码高亮
import 'highlight.js/styles/atom-one-dark.css'
import 'highlight.js/lib/common'
import hljsVuePlugin from '@highlightjs/vue-plugin'
app.use(hljsVuePlugin)

// 自定义样式
import '@/assets/main.scss'

app.mount('#app')
