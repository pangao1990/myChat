<template>
  <div>
    <!-- 对话列表 -->
    <div class="item" v-for="item in state.chatTitleList" :key="item" :class="{ 'select': state.selectTitle == item.title }" @click="onSelect(item.title)">
      <div class="center-c">
        <div class="item-title">{{ item.title }}</div>
        <div class="item-date right center-col">
          <div>{{ item.date }}</div>
          <div>{{ item.time }}</div>
        </div>
      </div>
      <div class="item-content">{{ item.theme }}</div>
    </div>
  </div>
</template>

<script setup>
import { reactive, computed } from 'vue'
import { useStoreAside } from '@/stores/aside'

const storeAside = useStoreAside()
const state = reactive({
  selectTitle: '',
  chatTitleList: []
})

state.chatTitleList = computed(() => {
  return storeAside.chatTitleInfoList
})
state.selectTitle = computed(() => {
  return storeAside.selectTitle
})

// 选择聊天主题
const onSelect = (title) => {
  storeAside.setSelectTitle(title)
}
</script>

<style scoped>
.item {
  padding: 12px;
  border-bottom: 1px solid #E4E7ED;
}

.select {
  background-color: #DEDEDE;
}

.item-title {
  color: #303133;
  font-weight: bold;
  width: 150px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.item-date {
  color: #909399;
  font-size: 10px;
}

.item-content {
  color: #909399;
  font-size: 12px;
  margin-top: 4px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
