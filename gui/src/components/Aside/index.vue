<template>
  <div class="aside">
    <div class="title">
      <div>
        {{ storeAside.appInfo.appName }}
        <span class="version">{{ storeAside.appInfo.appVersion }}</span>
      </div>

      <!-- 新增聊天列表 -->
      <el-button class="right" text key="plain" size="small" @click="onAddTitleDialog">
        <el-icon size="20">
          <ele-CirclePlus />
        </el-icon>
      </el-button>
      <AddTitleDialog :visible="state.visibleAddTitleDialog" @close="onCLoseAddTitleDialog" />
    </div>

    <!-- 主题列表 -->
    <TitleList class="scroll" />

    <!-- 设置 -->
    <div class="bottom">
      <MoreTools />
    </div>

  </div>
</template>

<script setup>
import AddTitleDialog from '@/components/Aside/AddTitleDialog.vue'
import TitleList from '@/components/Aside/TitleList.vue'
import MoreTools from '@/components/Aside/MoreTools/index.vue'
import { reactive } from 'vue'
import { useStoreAside } from '@/stores/aside'

const storeAside = useStoreAside()
const state = reactive({
  visibleAddTitleDialog: false
})

// 新增聊天列表
const onAddTitleDialog = () => {
  state.visibleAddTitleDialog = true
}
const onCLoseAddTitleDialog = (visible) => {
  state.visibleAddTitleDialog = visible
}
</script>

<style scoped>
.aside {
  width: 230px;
  border-right: 1px solid #E4E7ED;
}

.scroll {
  overflow: scroll;
  background-color: #F7F7F7;
  height: calc(100vh - 110px);
}

.title {
  display: flex;
  align-items: center;
  background-color: #F7F7F7;
  color: #303133;
  font-weight: bold;
  height: 60px;
  border-bottom: 1px solid #E4E7ED;
  padding-left: 18px;
  padding-right: 4px;
}

.version {
  color: #606266;
  margin-left: 2px;
  font-size: 12px;
}

.right {
  margin-left: auto;
}

.bottom {
  display: flex;
  align-items: center;
  background-color: #F7F7F7;
  color: #303133;
  font-weight: bold;
  height: 50px;
  border-top: 1px solid #E4E7ED;
  padding-left: 18px;
  padding-right: 18px;
}
</style>
