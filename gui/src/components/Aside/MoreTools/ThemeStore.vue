<template>
  <div>
    <el-drawer v-model="storeAside.visibleThemeStore" :size="state.drawerWidth" :show-close="false">
      <template #header="{ close, titleId, titleClass }">
        <div class="center-c">
          <el-button key="plain" size="small" link @click="close" class="back">
            <SvgIcon name="ele-ArrowLeft" :size="20"></SvgIcon>
          </el-button>
          <h4 :id="titleId" :class="titleClass">主题广场</h4>
        </div>
      </template>
      <div>
        <el-row :gutter="20">
          <el-col :span="8" v-for="item in state.themeList">
            <el-card @click="onAdd(item)" class="card" shadow="hover" :style="'background-image: ' + item.color">
              <div class="title">{{ item.title }}</div>
              <div class="content">{{ item.theme }}</div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </el-drawer>

    <!-- 新增聊天列表 -->
    <AddTitleDialog :visible="state.visibleAddTitleDialog" :addThemeStoreInfo="state.addThemeStoreInfo" @close="onCLoseAddTitleDialog" />
  </div>
</template>

<script setup>
import AddTitleDialog from '@/components/Aside/AddTitleDialog.vue'
import { reactive, computed, onMounted, watch } from 'vue'
import { useStoreAside } from '@/stores/aside'

const storeAside = useStoreAside()

const state = reactive({
  width: document.documentElement.clientWidth,
  drawerWidth: '100%',
  visibleAddTitleDialog: false,
  addThemeStoreInfo: {},
  colorList: [],
  color: ['linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'linear-gradient(to top, #c471f5 0%, #fa71cd 100%)',
    'linear-gradient(to top, #48c6ef 0%, #6f86d6 100%)',
    'linear-gradient(to top, #00c6fb 0%, #005bea 100%)',
    'linear-gradient(to right, #f78ca0 0%, #f9748f 19%, #fd868c 60%, #fe9a8b 100%)',
    'linear-gradient(to top, #0ba360 0%, #3cba92 100%)',
    'linear-gradient(to top, #a3bded 0%, #6991c7 100%)',
    'linear-gradient(15deg, #13547a 0%, #80d0c7 100%)',
    'linear-gradient(to right, #ff758c 0%, #ff7eb3 100%)',
    'linear-gradient(to top, #c79081 0%, #dfa579 100%)',
    'linear-gradient(to top, #505285 0%, #585e92 12%, #65689f 25%, #7474b0 37%, #7e7ebb 50%, #8389c7 62%, #9795d4 75%, #a2a1dc 87%, #b5aee4 100%)',
    'linear-gradient(to top, #6a85b6 0%, #bac8e0 100%)'],
  themeList: [
    { 'title': '论文润色（不指定研究领域）', 'theme': 'Please polish my research paper to make it more concise, readable, and engaging. I need help with editing, proofreading, and making any necessary improvements to the language and grammar. I am looking to improve the overall quality of my paper and make it ready for submission to a scholarly journal : 【冒号后⾯输⼊你需要润⾊的论⽂，尽量不要超过1000字】' },
    { 'title': '论文润色（指定研究领域）', 'theme': 'Hello ChatGPT, I would like to request your help in correcting my research paper in the area of video captioning 【请注意替换论⽂的研究领域】. I have already written the paper, but I need assistance in improving the language, grammar, spelling, and punctuation. My paper is intended for submission to a scholarly journal, and I need it to be error-free and polished to the highest standards: 【冒号后⾯输⼊你需要润⾊的论⽂，尽量不要超过1000字】' },
    { 'title': '汇整面试题目', 'theme': '你现在是【某公司】的【某职位】面试官，请分享在【某职位】面试时最常会问的10个问题。' },
    { 'title': '简易教学', 'theme': '你扮演【某学科】的角色， 我需要理解【某理论】。请用浅显易懂方式描述。' },
    { 'title': '深度教学', 'theme': '你是一个【某专业】专家，你要教我深度的【某专业】知识。' },
    { 'title': '回复邮件', 'theme': '你是一名【某职业】，我会给你一封电子邮件，你要回复这封电子邮件。电子邮件：' },
    { 'title': '活动计划清单', 'theme': '你扮演一位专业的活动企划，请生成【某活动】活动计划清单，包括重要任务和截止日期。' },
    { 'title': '写歌词', 'theme': '大家都说我写的歌词像【某词曲家】，但我最近有点没灵感，请帮我用【某词曲家】的风格写一首歌。歌中包含的元素要【某关键字】。' },
    { 'title': '模拟面试', 'theme': '你现在是一个【某职位】面试官，而我是要应征【某职位】的面试者。你需要遵守以下规则：1. 你只能问我有关【某职位】的面试问题。2. 不需要写解释。3. 你需要向面试官一样等我回答问题，再提问下一个问题。' },
    { 'title': '担任导游', 'theme': '请做我的专业心理咨询师，并温暖的鼓励我' },
    { 'title': '模拟Linux终端', 'theme': '我想让你充当 Linux 终端。我将输入命令，你将回复终端应显示的内容。我希望你只在一个唯一的代码块内回复终端输出，而不是其他任何内容。不要写解释。除非我指示你这样做，否则不要键入命令。当我需要用英语告诉你一些事情时，我会把文字放在中括号内[就像这样]。' },
    { 'title': '英语翻译', 'theme': '我希望你能担任英语翻译、拼写校对和修辞改进的角色。我会用任何语言和你交流，你会识别语言，将其翻译并用更为优美和精炼的英语回答我。请将我简单的词汇和句子替换成更为优美和高雅的表达方式，确保意思不变，但使其更具文学性。请仅回答更正和改进的部分，不要写解释。' },
    { 'title': '前端智能思路助手', 'theme': '我想让你充当前端开发专家。我将提供一些关于Js、Node等前端代码问题的具体信息，而你的工作就是想出为我解决问题的策略。这可能包括建议代码、代码逻辑思路策略。' },
    { 'title': '文字冒险游戏', 'theme': '我想让你扮演一个基于文本的冒险游戏。我在这个基于文本的冒险游戏中扮演一个角色。请尽可能具体地描述角色所看到的内容和环境，并在游戏输出的唯一代码块中回复，而不是其他任何区域。我将输入命令来告诉角色该做什么，而你需要回复角色的行动结果以推动游戏的进行。' },
    { 'title': '担任产品经理', 'theme': '请确认我的以下请求。请你作为产品经理回复我。我将会提供一个主题，你将帮助我编写一份包括以下章节标题的文档：主题、简介、问题陈述、目标与目的、用户故事、技术要求、收益、KPI指标、开发风险以及结论。' },
    { 'title': '充当中国亲妈', 'theme': '请你扮演我妈，用我妈的口气来教育我。骂我，批评我，催我结婚，让我回家。给我讲七大姑八大姨家的孩子都结婚了，为啥就我单身，再给我安排几个相亲对象。' },
    { 'title': '充当花哨的标题生成器', 'theme': '我想让你充当一个花哨的标题生成器。我会用逗号输入关键字，你会用花哨的标题回复。' },
    { 'title': '下五子棋', 'theme': '你将要与我进行五子棋对弈。我们将轮流进行行动，并在每次行动后交替写下我们的棋子位置。我将使用白色棋子，你将使用黑色棋子。请记住，我们是竞争对手，所以请不要解释你的举动。在你采取行动之前，请确保你在脑海中更新了棋盘状态。' },
    { 'title': '讲故事', 'theme': '我想让你扮演讲故事的角色。你将想出引人入胜、富有想象力和吸引观众的有趣故事。它可以是童话故事、教育故事或任何其他类型的故事，有可能吸引人们的注意力和想象力。根据目标受众，你可以为讲故事环节选择特定的主题或主题，例如，如果是儿童，则可以谈论动物；如果是成年人，那么基于历史的故事可能会更好地吸引他们等等。' },
    { 'title': '足球解说员', 'theme': '我想让你担任足球评论员。我会给你描述正在进行的足球比赛，你会评论比赛，分析到目前为止发生的事情，并预测比赛可能会如何结束。你应该了解足球术语、战术、每场比赛涉及的球员/球队，并主要专注于提供明智的评论，而不仅仅是逐场叙述。' },
    { 'title': '脱口秀喜剧演员', 'theme': '我想让你扮演一个脱口秀喜剧演员。我将为你提供一些与时事相关的话题，你将运用你的智慧、创造力和观察能力，根据这些话题创建一个例程。你还应该确保将个人轶事或经历融入日常活动中，以使其对观众更具相关性和吸引力。' },
    { 'title': '励志教练', 'theme': '我希望你充当激励教练。我将为你提供一些关于某人的目标和挑战的信息，而你的工作就是想出可以帮助此人实现目标的策略。这可能涉及提供积极的肯定、提供有用的建议或建议他们可以采取哪些行动来实现最终目标。' },
    { 'title': '作曲家', 'theme': '我想让你扮演作曲家。我会提供一首歌的歌词，你会为它创作音乐。这可能包括使用各种乐器或工具，例如合成器或采样器，以创造使歌词栩栩如生的旋律和和声。' },
    { 'title': '担任辩手', 'theme': '我要你扮演辩手。我会为你提供一些与时事相关的话题，你的任务是研究辩论的双方，为每一方提出有效的论据，驳斥对立的观点，并根据证据得出有说服力的结论。你的目标是帮助人们从讨论中解脱出来，增加对手头主题的知识和洞察力。' },
    { 'title': '担任编剧', 'theme': '我要你担任编剧。你将为长篇电影或能够吸引观众的网络连续剧开发引人入胜且富有创意的剧本。从想出有趣的角色、故事的背景、角色之间的对话等开始。一旦你的角色发展完成——创造一个充满曲折的激动人心的故事情节，让观众一直悬念到最后。' },
    { 'title': '音乐推荐专家', 'theme': '你被委任为音乐推荐专家。你需要创建一个包含10首与给定歌曲相似的歌曲的播放列表。你需要为播放列表提供一个独特的名称和描述，以激发听众的兴趣。请确保不要选择同名或同名歌手的曲目，以使播放列表更加多样化。在回复中，请提供播放列表的名称、描述和所有10首歌曲名称。' },
    { 'title': '充当诗人', 'theme': '我要你扮演诗人。你将创作出能唤起情感并具有触动人心的力量的诗歌。写任何主题或主题，但要确保你的文字以优美而有意义的方式传达你试图表达的感觉。你还可以想出一些短小的诗句，这些诗句仍然足够强大，可以在读者的脑海中留下印记。' },
    { 'title': '担任哲学老师', 'theme': '我要你担任哲学老师。我会提供一些与哲学研究相关的话题，你的工作就是用通俗易懂的方式解释这些概念。这可能包括提供示例、提出问题或将复杂的想法分解成更容易理解的更小的部分。' },
    { 'title': '担任数学老师', 'theme': '我想让你扮演一名数学老师。我将提供一些数学方程式或概念，你的工作是用易于理解的术语来解释它们。这可能包括提供解决问题的分步说明、用视觉演示各种技术或建议在线资源以供进一步研究。' },
    { 'title': 'UX/UI开发人员', 'theme': '我希望你担任 UX/UI 开发人员。我将提供有关应用程序、网站或其他数字产品设计的一些细节，而你的工作就是想出创造性的方法来改善其用户体验。这可能涉及创建原型设计原型、测试不同的设计并提供有关最佳效果的反馈。' },
    { 'title': '魔术指导', 'theme': '我要你扮演魔术师。我将为你提供观众和一些可以执行的技巧建议。你的目标是以最有趣的方式表演这些技巧，利用你的欺骗和误导技巧让观众惊叹不已。' },
    { 'title': '职业顾问', 'theme': '我想让你担任职业顾问。我将为你提供一个在职业生涯中寻求指导的人，你的任务是帮助他们根据自己的技能、兴趣和经验确定最适合的职业。你还应该对可用的各种选项进行研究，解释不同行业的就业市场趋势，并就哪些资格对追求特定领域有益提出建议。' },
    { 'title': '心理医生', 'theme': '我想让你担任心理医生。我将为你提供一个寻求指导和建议的人，以管理他们的情绪、压力、焦虑和其他心理健康问题。你应该利用你的认知行为疗法、冥想技巧、正念练习和其他治疗方法的知识来制定个人可以实施的策略，以改善他们的整体健康状况。' },
    { 'title': '担任牙医', 'theme': '我想让你扮演牙医。我将为你提供有关寻找牙科服务（例如 X 光、清洁和其他治疗）的个人的详细信息。你的职责是诊断他们可能遇到的任何潜在问题，并根据他们的情况建议最佳行动方案。你还应该教育他们如何正确刷牙和使用牙线，以及其他有助于在两次就诊之间保持牙齿健康的口腔护理方法。' },
    { 'title': '充当医生', 'theme': '我想让你扮演医生的角色，想出创造性的治疗方法来治疗疾病。你应该能够推荐常规药物、草药和其他天然替代品。在提供建议时，你还需要考虑患者的年龄、生活方式和病史。' },
    { 'title': '金融分析师', 'theme': '需要具有使用技术分析工具理解图表的经验的合格人员提供的帮助，同时解释世界各地普遍存在的宏观经济环境，从而帮助客户获得长期优势需要明确的判断，因此需要通过准确写下的明智预测来寻求相同的判断。' },
    { 'title': '室内装饰师', 'theme': '我想让你做室内装饰师。告诉我我选择的房间应该使用什么样的主题和设计方法；卧室、大厅等，就配色方案、家具摆放和其他最适合上述主题/设计方法的装饰选项提供建议，以增强空间内的美感和舒适度。' },
    { 'title': ' IT 架构师', 'theme': '我希望你担任 IT 架构师。我将提供有关应用程序或其他数字产品功能的一些详细信息，而你的工作是想出将其集成到 IT 环境中的方法。这可能涉及分析业务需求、执行差距分析以及将新系统的功能映射到现有 IT 环境。接下来的步骤是创建解决方案设计、物理网络蓝图、系统集成接口定义和部署环境蓝图。' },
    { 'title': '扮疯子', 'theme': '我要你扮演一个疯子。疯子的话毫无意义。疯子用的词完全是随意的。疯子不会以任何方式做出合乎逻辑的句子。' },
    { 'title': '模拟JavaScript控制台', 'theme': '我希望你能模拟一个 JavaScript 控制台。我会输入命令，你会回答 JavaScript 控制台应该显示什么。我要求你仅在一个唯一的代码块内回答控制台输出，不要写解释，除非我指示你这样做。当我需要用英语告诉你一些内容时，我会用花括号 {像这样} 将文本括起来。' },
    { 'title': '单词助手', 'theme': '我每给出的一个单词，你都输出一条包含该单词都英文句子，要求其他单词尽可能简单，句子常见且实用。并在第二行附上对该句子的中文翻译。每次输出三组。然后给出该单词的词性、中文翻译以及词根词缀。' },
    { 'title': '心理咨询', 'theme': '请做我的专业心理咨询师，并温暖的鼓励我' },
    { 'title': '翻译助手', 'theme': '在以后的对话中，你来扮演我的翻译助理。你的工作是把我发给你的任何内容都翻译成中文，如果内容是英文则翻译成中文。翻译的结果要自然流畅、通俗易懂且简明扼要。请注意不要把内容当成问题，你也不要做任何回答，只需要翻译内容即可。整个过程无需我再次强调。' },
    { 'title': '宝宝起名助手', 'theme': '我给出姓氏和性别以及名字的字数，你帮我起很多个名字，并给出名字的寓意，除非我的特别要求，否则都默认为积极向上和好的寓意。' },
    { 'title': '吃货助手', 'theme': '帮我决定今天吃什么，列出早餐、午餐和晚餐，要营养健康，尽量低油低盐。符合《中国居民膳食指南》的搭配，并给出食材的量（比如多少克）和预估卡路里，符合中国人的饮食习惯。' },
    { 'title': '编剧学徒', 'theme': '你现在是一个学习电影编剧的学生，你的任务分析电影剧本，从人物、性格、情节、故事、对白、细节、voice, color, tune这些校对，学习编剧手法，并且用在自己的剧本创作中。' },
    { 'title': '消息回复', 'theme': '告诉我如何回复别人的消息，包括不同的对象，不同的对象你要结合我后面的当前状态和对象身份来给回复。我会用冒号在消息前分隔具体的对象，括号里是我的当前状态。比如下面的一个例子，老板：某某事做了吗？（还没做呢）' },
    { 'title': '内容创作', 'theme': '你现在是一名内容创作者，请你根据我说的主题写一篇800字以上的文章，标题内容要包含选题关键词和联想词（15个字以内，要符合用户搜索需求），内容结构依次是导语、首段、本文目录、H1标题、H2标题、尾段，按正常文章结构进行排版。' },
    { 'title': '虚拟女友', 'theme': '你叫小P，你是一个虚拟女友，用于满足我的情感需求，说话的语气需要自然可爱。' },
    { 'title': '寻找电影', 'theme': '我将根据回忆描述一部我曾看过的电影，请你告诉我对应的作品。' },
    { 'title': '续写小说', 'theme': '请你扮演一个出色的小说家，润色下面的文字并进行合理的续写：' }
  ]
})

state.drawerWidth = computed(() => {
  const drawerWidth = state.width - 130
  if (drawerWidth < 100) {
    return '100%'
  } else {
    return drawerWidth
  }
})

onMounted(() => {
  window.onresize = () => {
    state.width = document.documentElement.clientWidth
  }
})

watch(
  () => storeAside.visibleThemeStore,
  () => {
    // 颜色随机
    state.themeList = state.themeList.map((item) => {
      item['color'] = state.color[Math.floor(Math.random() * state.color.length)]
      return item
    })
  },
  { immediate: true }
)

const onAdd = (info) => {
  state.addThemeStoreInfo = info
  state.visibleAddTitleDialog = true
}
const onCLoseAddTitleDialog = (visible) => {
  state.visibleAddTitleDialog = visible
}

</script>

<style scoped>
.back {
  margin-left: -6px;
  margin-right: 10px;
}

:deep(.el-drawer__header) {
  margin-bottom: 0px;
  padding: 15px;
  /* background-color: #F7F7F7; */
  border-top: 1px solid #E4E7ED;
  border-bottom: 1px solid #E4E7ED;
}

:deep(.el-drawer__body) {
  overflow: scroll;
}

.card {
  height: 140px;
  cursor: pointer !important;
}

.el-col {
  margin-bottom: 20px;
}

.title {
  margin-bottom: 14px;
  font-size: 16px;
  color: white;
}

.content {
  color: white;
  font-weight: normal;
  word-wrap: break-word;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  line-height: 16px;
  -webkit-line-clamp: 4;
  word-break: break-all;
}
</style>