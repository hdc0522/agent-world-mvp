# Agent World - Design Specification

## 1. Concept & Vision

**"暗黑奇幻放置RPG"** — 一款讲述从幼儿园到25岁人生旅程的放置游戏。
视觉风格：**暗黑地下室 + 日系立绘 + 手游质感**。
核心理念：每一次等待都有意义，每一次升级都有仪式感，每一件装备都是惊喜。

---

## 2. Color Palette

```
背景主色:     #08080F  (深空黑紫)
卡片背景:     #13131F  (暗夜紫)
卡片悬停:     #1A1A2E  (略亮)
边框线:       #2A2A4A  (暗紫边框)
金色主:       #C9A227  (皇室金)
金色亮:       #E8C547  (发光金)
金色暗:       #8B7234  (暗金)
治疗绿:       #3DD68C  (翠绿)
坦克蓝:       #5A8FBD  (钢蓝)
输出红:       #C44536  (血红)
危险红:       #DC3545
文字主:       #E8E4D9  (暖白)
文字次:       #9A968A  (灰白)
文字暗:       #5A5850
白色:         #B8B8B8  (白装)
绿色:         #3DD68C  (绿装)
蓝色:         #4A9EFF  (蓝装)
紫色:         #B87DD4  (紫装)
金色:         #FFD700  (金装)
```

---

## 3. Typography

- **标题/Logo**: `Cinzel` (Google Fonts) — 暗黑奇幻感西文衬线
- **中文字体**: `Noto Sans SC` — 清晰现代中文
- **数字/Stats**: `Orbitron` — 科幻感数字，用于等级/金币等
- **Fallback**: `system-ui, sans-serif`

---

## 4. Layout System

- 设备最大宽度: **480px**（移动优先）
- 页面内边距: **16px**
- 卡片圆角: **12px**
- 按钮圆角: **8px**
- 间距基准: **8px**（8/16/24/32）

---

## 5. Component Specifications

### 5.1 Top Status Bar (固定顶部)
```
高度: 56px
背景: linear-gradient(#13131F, #08080F)
底部: 1px solid #2A2A4A
左侧: 等级图标 + 等级数字 (Orbitron字体, 金色)
中间: 阶段名称 (幼儿园/小学...)
右侧: 金币图标 + 金币数
邮件图标带未读角标
```

### 5.2 Title Screen
```
- 背景: 深色粒子星空 (CSS动画)
- Logo: "AGENT WORLD" Cinzel字体, 金色渐变, 微微发光动画
- 副标题: "25岁人生模拟器" 暗金色
- 介绍卡片: 4步流程 (带序号圆点)
- 按钮: "开始测试" 金色渐变按钮, 大尺寸, hover时发光
- "继续游戏": 次级样式, 有存档时显示
- 存档预览卡: 显示职业/等级/阶段
```

### 5.3 MTI Quiz Screen
```
进度条: 4个圆点, 完成=绿色填充, 当前=绿色脉冲, 未完成=暗边框
题目卡片: 背景#13131F, 圆角12px, 内边距24px
选项: 垂直列表, 每项背景#08080F, hover时左边框金色滑入
选中态: 左边框4px金色, 背景微亮
字体: 题目20px粗体, 选项16px
```

### 5.4 Result Screen (最重要!)
```
全屏中央, 深色渐变背景 + 粒子
角色大图: 200x200, 圆角12px, 金色外发光边框, 呼吸动画
职业徽章: 圆角pill, 职业对应颜色背景, 居中底部
金色分隔线 + 职业名称 (32px Cinzel)
描述文字 (14px, 暗金色)
MTI标签: 小字, 右上角
"进入游戏"按钮: 全宽, 金色渐变, 36px高度
```

### 5.5 Idle Screen (挂机主页)
```
顶部: 角色立绘 (140px高, 呼吸动画)
等级: 大号Orbitron字体, 金色
阶段名: 彩色文字 (幼儿园=黄色, 小学=橙色...)
经验条: 圆角条, 绿色渐变填充, 顶部高光
当前/所需经验文字
金币/秒统计

等待按钮区:
- 3个按钮并排: 30秒/1分钟/3分钟
- 各自不同颜色边框对应职业色
- 显示预估奖励
- hover时背景亮起

底部导航: 5个图标按钮 (主页/角色/背包/邮件/排行)
```

### 5.6 Dungeon Screen
```
顶部: 当前层数 (大字)
敌我HP条: 渐变填充 (绿→红), 带数字
敌人区域: 怪物图/占位, 抖动动画
战斗日志: 滚动文字区
操作按钮: 攻击/治疗/特殊技能
```

### 5.7 Backpack/Equipment Screen
```
左侧(60%): 角色立绘 + 装备槽
  - 头部/胸甲/腿甲/靴子/手套/披风/饰品 (左侧)
  - 主手/副手 (底部)

右侧(40%): 统计面板
  - ATK/DEF/HP数值条
  - 对比高亮 (+X green / -X red)

装备列表: 卡片网格, 品质边框颜色
```

### 5.8 Mail Modal
```
居中弹窗, 深色背景, 金色标题栏
邮件列表: 每封邮件可点击
未读: 左边金色竖线
已领取: 灰暗
```

### 5.9 Reward Popup (挂机结束)
```
居中弹出
奖励区: 经验/金币/装备卡片
装备卡片: 品质边框 + 属性 + 图标
收下按钮: 金色
关闭动画: 淡出
```

---

## 6. Animation System

### 全局
- 页面切换: `fadeIn 0.3s ease`
- 按钮悬停: `transform: translateY(-2px)`, `box-shadow`发光

### 呼吸/浮动
```css
@keyframes breathe {
  0%, 100% { transform: scale(1) translateY(0); }
  50% { transform: scale(1.02) translateY(-4px); }
}
```

### 伤害飘字
```css
@keyframes damageFloat {
  0% { opacity: 1; transform: translateY(0) scale(1); }
  50% { opacity: 1; transform: translateY(-30px) scale(1.2); }
  100% { opacity: 0; transform: translateY(-50px) scale(0.8); }
}
```

### 暴击星星
```css
@keyframes starBurst {
  0% { transform: scale(0) rotate(0deg); opacity: 1; }
  100% { transform: scale(2) rotate(180deg); opacity: 0; }
}
```

### 升级光环
```css
@keyframes levelUpGlow {
  0% { box-shadow: 0 0 0 0 rgba(201, 162, 39, 0.8); }
  100% { box-shadow: 0 0 0 30px rgba(201, 162, 39, 0); }
}
```

### 装备获得闪烁
```css
@keyframes equipGlow {
  0%, 100% { box-shadow: 0 0 5px rgba(255, 215, 0, 0.3); }
  50% { box-shadow: 0 0 25px rgba(255, 215, 0, 0.8); }
}
```

### 经验条填充
```css
@keyframes expFillPulse {
  0%, 100% { filter: brightness(1); }
  50% { filter: brightness(1.4); }
}
```

### 星星粒子背景
```css
@keyframes starFloat {
  0% { transform: translateY(0); opacity: 0.3; }
  50% { opacity: 1; }
  100% { transform: translateY(-100vh); opacity: 0.3; }
}
```

---

## 7. Quality Colors (装备品质)

```
white:  #B8B8B8  (普通)
green:  #3DD68C  (优秀) + green glow
blue:   #4A9EFF  (精良) + blue glow
purple: #B87DD4  (史诗) + purple glow + particle effect
gold:   #FFD700  (传说) + gold glow + shimmer animation
```

---

## 8. Game Balance

### 挂机经验
```
30秒: baseExp = 20 + level*5
60秒: baseExp = 45 + level*8
180秒: baseExp = 100 + level*15

升级公式: levelUpExp = level * 100
```

### 副本等级门槛
```
副本1 (森林废墟): Lv.1 (降门槛!)
副本2: Lv.3
副本3: Lv.6
副本4: Lv.10
副本5: Lv.15
副本6: Lv.21
```

### 暴击系统
```
暴击率: 15%
暴击伤害: 200%
暴击特效: 金色数字 + 星星爆发
```

---

## 9. Accessibility

- 所有交互元素有:focus状态
- 颜色对比度 AA 标准
- 按钮最小点击区域 44x44px
- 进度/动画不遮挡内容
