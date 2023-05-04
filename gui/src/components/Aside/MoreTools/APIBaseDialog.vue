<template>
  <div>
    <!-- 自定义API地址 -->
    <el-dialog v-model="state.setDialogVisible" title="自定义API地址" align-center draggable destroy-on-close :close-on-click-modal="false" :close-on-press-escape="false" :show-close="false">
      <el-form label-position="right" label-width="60px">
        <el-form-item label="https://">
          <el-input v-model="state.apiBase" placeholder="api.openai.com" />
        </el-form-item>
      </el-form>
      <div class="tip">默认使用官方API地址 api.openai.com。当然，也可以自定义API地址。</div>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="onCancel">取消</el-button>
          <el-button type="primary" @click="onSetConfirm">确认</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
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
const emits = defineEmits(['close'])

const state = reactive({
  setDialogVisible: false,
  apiBase: '', // 自定义API地址
})

watch(
  () => props.visible,
  (visible) => {
    if (visible) {
      onSet() // 设置
    }
  }
)

const onSet = async () => {
  // 设置
  state.setDialogVisible = true
  state.apiBase = await window.pywebview.api.storage_get('apiBase')
}

const onCancel = () => {
  state.setDialogVisible = false
  emits('close', state.setDialogVisible)
}

const onSetConfirm = () => {
  // console.log(state.apiBase)
  state.setDialogVisible = false
  window.pywebview.api.storage_set('apiBase', state.apiBase)
  emits('close', state.setDialogVisible)
}

</script>

<style scoped>
.tip {
  color: #909399;
  font-size: 12px;
}
</style>
