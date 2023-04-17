<template>
  <div>
    <!-- 设置代理 -->
    <el-dialog v-model="state.setSSHDialogVisible" title="设置代理" align-center draggable destroy-on-close :close-on-click-modal="false" :close-on-press-escape="false" :show-close="false">
      <el-form label-position="right" label-width="50px">
        <el-form-item label="http://">
          <el-row>
            <el-col :span="13">
              <el-input v-model="state.proxyIP" placeholder="IP地址" />
            </el-col>
            <el-col :span="1" class="center-col">
              :
            </el-col>
            <el-col :span="10">
              <el-input v-model="state.proxyPort" placeholder="端口" />
            </el-col>
          </el-row>
        </el-form-item>
      </el-form>
      <div class="tip">默认不需要设置IP地址和端口，程序自动获取系统代理设置。若系统代理已经启动，但本程序仍然无法访问OpenAI，请手动设置代理IP地址和端口。</div>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="onCancel">取消</el-button>
          <el-button type="primary" @click="onSetSSHConfirm">确认</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ElMessage } from 'element-plus'
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
  setSSHDialogVisible: false,
  proxyIP: '127.0.0.1', // 代理IP
  proxyPort: '', // 代理端口
  proxyIPs: '127.0.0.1', // 代理IPs
  proxyPorts: '', // 代理端口s
})

watch(
  () => props.visible,
  (visible) => {
    if (visible) {
      onSSH() // 设置代理
    }
  }
)

const onSSH = async () => {
  // 设置代理
  state.setSSHDialogVisible = true
  state.proxyIP = await window.pywebview.api.storage_get('proxyIP')
  state.proxyPort = await window.pywebview.api.storage_get('proxyPort')
}

const onCancel = () => {
  state.setSSHDialogVisible = false
  emits('close', state.setSSHDialogVisible)
}

const onSetSSHConfirm = () => {
  // console.log(state.proxyPort, state.proxyPorts)
  if (state.proxyIP == '' && state.proxyPort != '') {
    ElMessage({ type: 'warning', message: '请设置IP地址信息', grouping: true })
  } else if (state.proxyIP != '' && state.proxyPort == '') {
    ElMessage({ type: 'warning', message: '请设置端口信息', grouping: true })
  } else {
    state.setSSHDialogVisible = false
    window.pywebview.api.storage_set('proxyIP', state.proxyIP)
    window.pywebview.api.storage_set('proxyPort', state.proxyPort)
    emits('close', state.setSSHDialogVisible)
  }
}

</script>

<style scoped>
.tip {
  color: #909399;
  font-size: 12px;
}
</style>
