<template>
  <div>
    <!-- 新增聊天列表 -->
    <el-dialog v-model="state.visible" :title="props.edit ? '编辑聊天类型' : '新增聊天类型'" align-center draggable destroy-on-close :close-on-click-modal="false" :close-on-press-escape="false" :show-close="false">
      <el-form>
        <el-form-item label="聊天标题">
          <el-input :disabled="props.edit" v-model="state.addTitle" placeholder="（仅为方便使用者标记分类）" clearable />
        </el-form-item>
        <el-form-item label="聊天主题">
          <el-input :disabled="props.edit" v-model="state.addTheme" type="textarea" :autosize="{ minRows: 1, maxRows: 4 }" placeholder="（该主题信息将会发送给AI，请尽量详细描述）" />
        </el-form-item>
        <div v-if="!props.edit" class="select-title">
          <span class="label">或选择主题</span>
          <el-button plain size="small" @click="onAddTheme('请将我说的话翻译成英文')">请将我说的话翻译成英文</el-button>
          <el-button plain size="small" @click="onAddTheme('请润色我说的每一句话')">请润色我说的每一句话</el-button>
        </div>
        <el-form-item label="GPT模型">
          <el-select v-model="state.addModel" placeholder="请选择GPT模型">
            <el-option v-for="item in state.modelList" :key="item.name" :label="item.name" :value="item.name">
              <el-tooltip placement="left">
                <template #content>
                  <div class="tip-model">{{ item.info }}</div>
                </template>
                <span style="float: left;width: 100%;">{{ item.name }}</span>
              </el-tooltip>
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="记忆消息个数">
          <el-select v-model="state.addNewsCount" placeholder="请选择记忆消息个数" style="width: 80px;">
            <el-option v-for="item in state.newsCountList" :key="item" :label="item" :value="item" />
          </el-select>
          <el-tooltip placement="right">
            <template #content>
              <div class="tip-model">选择【0】则表示每次都是独立对话，并不参考历史对话信息；选择【全部】则表示会参考全部历史内容作出回答。</div>
            </template>
            <SvgIcon name="ele-Warning" :size="16" class="ml10 cursor-pointer"></SvgIcon>
          </el-tooltip>
        </el-form-item>
        <el-form-item label="模型参数">
          <el-slider v-model="state.addTemperature" :max="2" :step="0.1" :marks="state.temperatureMarks" />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="onCancel">取消</el-button>
          <el-button type="primary" @click="onConfirm">确认</el-button>
        </span>
      </template>
    </el-dialog>

  </div>
</template>

<script setup>
import { ElMessage } from 'element-plus'
import { reactive, watch } from 'vue'
import * as dates from '@/utils/dates'
import { useStoreAside } from '@/stores/aside'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false,
    required: false
  },
  edit: {
    type: Boolean,
    default: false,
    required: false
  },
  addThemeStoreInfo: {
    type: Object,
    default: {},
    required: false
  }
})
const emits = defineEmits(['close'])

const storeAside = useStoreAside()
const state = reactive({
  visible: false,
  addTitle: '',
  addTheme: '',
  addModel: 'gpt-3.5-turbo',
  modelList: [],
  addTemperature: 1,
  temperatureMarks: {
    0.2: { style: { color: '#67C23A', }, label: '确定性', },
    1: { style: { color: '#1989FA', }, label: '平衡', },
    1.8: { style: { color: '#F56C6C', }, label: '创造力', }
  },
  addNewsCount: 0,
  newsCountList: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '全部']
})

watch(
  () => props.visible,
  (visible) => {
    if (visible) {
      onAdd() // 新增聊天列表
    }
  }
)

// 新增聊天列表
const onAdd = () => {
  state.visible = true
  // 获取模型列表
  window.pywebview.api.chat_getModelList().then((res) => {
    // console.log('chat_getModelList', res)
    state.modelList = res
  })
  if (props.edit) {
    state.addTitle = storeAside.selectTitleInfo.title
    state.addTheme = storeAside.selectTitleInfo.theme
    state.addModel = storeAside.selectTitleInfo.model
    state.addTemperature = storeAside.selectTitleInfo.temperature
    state.addNewsCount = storeAside.selectTitleInfo.news_count
  }
  if (JSON.stringify(props.addThemeStoreInfo) != "{}") {
    if (props.addThemeStoreInfo.title != undefined) {
      state.addTitle = props.addThemeStoreInfo.title
    }
    if (props.addThemeStoreInfo.theme != undefined) {
      state.addTheme = props.addThemeStoreInfo.theme
    }
    if (props.addThemeStoreInfo.model != undefined) {
      state.addModel = props.addThemeStoreInfo.model
    }
    if (props.addThemeStoreInfo.temperature != undefined) {
      state.addTemperature = props.addThemeStoreInfo.temperature
    }
    if (props.addThemeStoreInfo.news_count != undefined) {
      state.addNewsCount = props.addThemeStoreInfo.news_count
    }
  }
}

const onAddTheme = (val) => {
  state.addTheme = val
}

const onCancel = () => {
  state.visible = false
  emits('close', state.visible)
}

const onConfirm = () => {
  const chatTitleList = storeAside.chatTitleInfoList.map((item) => {
    return item.title
  })
  if (state.addTitle == '') {
    ElMessage({ type: 'warning', message: '请输入聊天标题', grouping: true })
  } else if (state.addTheme == '') {
    ElMessage({ type: 'warning', message: '请输入聊天主题', grouping: true })
  } else if (!props.edit && chatTitleList.indexOf(state.addTitle) > -1) {
    ElMessage({ type: 'warning', message: '该聊天标题已存在，请修改！', grouping: true })
  } else {
    state.visible = false
    const toDay = dates.formatDateThis(new Date())
    const date = toDay.slice(0, 10).replaceAll('-', '/')
    const time = toDay.slice(11, 16)
    if (props.edit) {
      const addInfo = { 'title': state.addTitle, 'theme': state.addTheme, 'model': state.addModel, 'temperature': state.addTemperature, 'news_count': state.addNewsCount }
      storeAside.updateChatTitleList(state.addTitle, addInfo)
    } else {
      const addInfo = { 'title': state.addTitle, 'theme': state.addTheme, 'model': state.addModel, 'temperature': state.addTemperature, 'news_count': state.addNewsCount, 'date': date, 'time': time }
      storeAside.addChatTitleInfoList(addInfo)
    }
    storeAside.setSelectTitle(state.addTitle)
    state.addTitle = ''
    state.addTheme = ''
    state.addModel = 'gpt-3.5-turbo'
    state.addTemperature = 1
    state.addNewsCount = 0
    emits('close', state.visible)
  }
}


</script>


<style scoped lang="scss">
.select-title {
  margin-top: -10px;
  margin-bottom: 15px;

  .label {
    color: #A8ABB2;
    font-size: 12px;
    margin-right: 6px;
  }
}

.tip-model {
  width: 200px;
}
</style>
