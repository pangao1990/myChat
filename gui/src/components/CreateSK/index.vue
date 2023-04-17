<template>
  <el-dialog v-model="state.visible" title="提示消息" width="38%" draggable top="40vh" destroy-on-close :close-on-click-modal="false" :close-on-press-escape="false" :show-close="false">
    <div class="mb4 ml4">请输入openAI的sk码</div>
    <el-input v-model="state.input" placeholder="sk-XXXXXXXXXXXXXXXX" clearable />
    <el-link class="ml6 mt4 font11" type="primary" href="https://blog.pangao.vip/超详细注册OpenAI接口账号的教程/" target="_blank">点击获取sk码</el-link>
    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="onConfirm">确定</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { reactive, watch } from 'vue'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false,
    required: false
  }
})

const state = reactive({
  visible: false,
  input: ''
})

watch(
  () => props.visible,
  (val) => {
    state.visible = val
  },
  { immediate: true }
)

const onConfirm = () => {
  state.visible = false
  window.pywebview.api.storage_set('skOpenAI', state.input)
}

</script>

<style scoped></style>
