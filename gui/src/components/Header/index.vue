<template>
  <div class="header center-c">
    <el-popover placement="bottom-start" :title="storeAside.selectTitleInfo.title" :content="storeAside.selectTitleInfo.theme" width="400" trigger="click">
      <template #reference>
        <div class="cursor-pointer">
          <div class="header-title">{{ storeAside.selectTitleInfo.title }}</div>
          <div class="header-content">{{ storeAside.selectTitleInfo.theme }}</div>
        </div>
      </template>
    </el-popover>

    <el-dropdown trigger="click" class="right">
      <span class="el-dropdown-link">
        <el-icon><ele-MoreFilled /></el-icon>
        <el-icon class="el-icon--right"><ele-ArrowDown /></el-icon>
      </span>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item @click="onEdit">
            <el-icon>
              <ele-Edit />
            </el-icon>
            修改模型
          </el-dropdown-item>
          <el-dropdown-item @click="onClear">
            <el-icon>
              <ele-ChatRound />
            </el-icon>
            清空消息
          </el-dropdown-item>
          <el-dropdown-item divided v-if="storeAside.selectTitleInfo.title != '随便聊聊'" @click="onDelete">
            <el-icon>
              <ele-Delete />
            </el-icon>
            删除对话
          </el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>

    <!-- 修改模型信息 -->
    <AddTitleDialog :visible="state.visibleAddTitleDialog" :edit="true" @close="onCLoseAddTitleDialog" />
  </div>
</template>

<script>
export default {
  name: ''
}
</script>

<script setup>
import AddTitleDialog from '@/components/Aside/AddTitleDialog.vue'
import { reactive, computed } from 'vue'
import { useStoreAside } from '@/stores/aside'

const storeAside = useStoreAside()
const emit = defineEmits(['onClear'])

const state = reactive({
  selectTitleInfo: {},
  visibleAddTitleDialog: false
})

state.selectTitleInfo = computed(() => {
  return storeAside.selectTitleInfo
})

// 修改模型
const onEdit = () => {
  state.visibleAddTitleDialog = true
}
const onCLoseAddTitleDialog = (visible) => {
  state.visibleAddTitleDialog = visible
}

// 清空消息
const onClear = () => {
  window.pywebview.api.chat_clearContent(state.selectTitleInfo.title)
  emit('onClear')
}

// 删除对话
const onDelete = () => {
  const selectTitle = storeAside.selectTitleInfo.title
  storeAside.setSelectTitle('随便聊聊')
  storeAside.deleteChatTitleList(selectTitle)
}
</script>

<style scoped>
.header {
  height: 60px;
  background-color: #F3F3F3;
  padding-left: 20px;
  padding-right: 20px;
  border-bottom: 1px solid #E4E7ED;
}


.header-title {
  color: #303133;
  font-weight: bold;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  width: calc(100vw - 400px);
}

.header-content {
  color: #909399;
  font-size: 12px;
  margin-top: 4px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  width: calc(100vw - 400px);
}

.right {
  margin-left: auto;
  cursor: pointer !important;
}
</style>
