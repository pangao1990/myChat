// 使用时，先 import * as dates from '@/utils/dates'

/*
 **  获取当前时间戳
 */
export function getTimest() {
  var tmp = Date.parse(new Date()).toString()
  tmp = tmp.substr(0, 10)
  return parseInt(tmp)
}

// 日期转时间戳
export function getUnixTime(dateStr) {
  var newstr = dateStr.replace(/-/g, '/')
  var date = new Date(newstr)
  var time_str = date.getTime().toString()
  return time_str.substr(0, 10)
}

// 时间戳转日期,falg:true表示只要年月日,part: year month date
export function toDate(number, flag = false, part = '') {
  var n = number
  var date = new Date(parseInt(n) * 1000)
  var y = date.getFullYear()
  var m = date.getMonth() + 1
  m = m < 10 ? '0' + m : m
  var d = date.getDate()
  d = d < 10 ? '0' + d : d
  var h = date.getHours()
  h = h < 10 ? '0' + h : h
  var minute = date.getMinutes()
  var second = date.getSeconds()
  minute = minute < 10 ? '0' + minute : minute
  second = second < 10 ? '0' + second : second
  if (flag) {
    if (part === 'year') {
      return y
    } else if (part === 'month') {
      return m
    } else if (part === 'date') {
      return n
    }
    return y + '-' + m + '-' + d
  }
  return y + '-' + m + '-' + d + ' ' + h + ':' + minute + ':' + second
}

// 判断两个日期时间戳相差多少天,参数为时间戳
export function timeStampCompare(dateTimeStamp1, dateTimeStamp2) {
  var dayNum = 0
  if (dateTimeStamp1 > dateTimeStamp2) {
    dayNum = Math.floor((dateTimeStamp1 - dateTimeStamp2) / 86400)
  } else {
    dayNum = Math.floor((dateTimeStamp2 - dateTimeStamp1) / 86400)
  }
  return dayNum
}

// 判断某个日期时间距今相差多少天,参数为日期
export function dateCompareNow(oneDate) {
  var dateTimeStamp1 = getUnixTime(oneDate)
  var now = getUnixTime(formatDateThis(new Date()))
  return timeStampCompare(dateTimeStamp1, now)
}

// 判断两个日期时间戳相差多少天,参数为日期
export function dateCompare(date1, date2) {
  var dateTimeStamp1 = getUnixTime(date1)
  var dateTimeStamp2 = getUnixTime(date2)
  return timeStampCompare(dateTimeStamp1, dateTimeStamp2)
}

// 判断过去某个时间点到当前时间是否达到多少天,可以用来定期清理缓存
export function datePassDays(dateTimeStamp, days) {
  var now = getUnixTime(formatDateThis(new Date()))
  var diffValue = now - dateTimeStamp
  var limitTime = days * 86400
  if (diffValue >= limitTime) {
    return true
  }
  return false
}

// 当前日期加减天数,falg:true表示只要年月日
export function mathChangeDate(date, method, days, flag) {
  // method:'+' || '-'
  // ios不解析带'-'的日期格式，要转成'/'，不然Nan，切记
  var dateVal = date.replace(/-/g, '/')
  var timestamp = Date.parse(dateVal)
  if (method === '+') {
    timestamp = timestamp / 1000 + 24 * 60 * 60 * days
  } else if (method === '-') {
    timestamp = timestamp / 1000 - 24 * 60 * 60 * days
  }
  return toDate(timestamp, flag)
}

// 时间戳转换具体时间描述(传入数值型时间戳)
export function getDateDiff(dateTimeStamp) {
  var result = ''
  var minute = 1 * 60
  var hour = minute * 60
  var day = hour * 24
  var month = day * 30
  var now = getUnixTime(formatDateThis(new Date())) // 有些特殊 不能使用 new Date()
  var diffValue = now - dateTimeStamp
  if (diffValue < 0) {
    return
  }
  var monthC = diffValue / month
  var weekC = diffValue / (7 * day)
  var dayC = diffValue / day
  var hourC = diffValue / hour
  var minC = diffValue / minute

  if (monthC >= 1) {
    result = '' + parseInt(monthC) + '月前'
  } else if (weekC >= 1) {
    result = '' + parseInt(weekC) + '周前'
  } else if (dayC >= 1) {
    result = '' + parseInt(dayC) + '天前'
  } else if (hourC >= 1) {
    result = '' + parseInt(hourC) + '小时前'
  } else if (minC >= 1) {
    result = '' + parseInt(minC) + '分钟前'
  } else {
    result = '刚刚'
  }
  return result
}

// 获取当前年份，月份， 例： getCurrentTime("year")
export const getCurrentTime = (method) => {
  const date = new Date()
  if (method === 'year') {
    return date.getFullYear()
  } else if (method === 'month') {
    return date.getMonth() + 1
  }
  return date
}

// 获取当前服务器时间,参数直接用 new Date() 就可以了
export const formatDateThis = (date) => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()
  return [year, month, day].map(formatNumber).join('-') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

export const formatTime = (date) => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  return [year, month, day].map(formatNumber).join('-')
}
export const formatTimeYesterday = (date) => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  return [year, month, day].map(formatNumber).join('-')
}
export const formatTimeTomorrow = (date) => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  return [year, month, day].map(formatNumber).join('-')
}

export const formatTimes = (time) => {
  const hour = time.getHours()
  const minute = time.getMinutes()
  const second = time.getSeconds()
  return [hour, minute, second].map(formatNumber).join(':')
}
// 补0
const formatNumber = (n) => {
  n = n.toString()
  return n[1] ? n : '0' + n
}

// 比较两个时间大小(格式参考yyyy-mm-dd hh:mm:ss)
export function compareTime(startTime, endTime) {
  // 结束时间大于开始时间就是true  ， 反之则为 false
  var sn = getUnixTime(startTime) * 1
  var en = getUnixTime(endTime) * 1
  if (en > sn) {
    return true
  }
  return false
}

// 判断是 上午，下午，晚上
export const getTimeState = (date) => {
  // 获取当前小时
  const hours = date.getHours()
  // 设置默认文字
  let text = ''
  // 判断当前时间段
  if (hours >= 0 && hours < 8) {
    text = '晚上'
  } else if (hours >= 8 && hours < 16) {
    text = '上午'
  } else if (hours >= 16 && hours < 0) {
    text = '下午'
  }
  // 返回当前时间段对应的状态
  return text
}
