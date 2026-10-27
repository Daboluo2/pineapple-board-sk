# 模块专用规则

把相关条目追加到三段式通用模板；只加载当前需要的模块，不要求每页包含全部模块。

| 模块 | 正面要求 | 负面要求 | 补充英文 |
|---|---|---|---|
| 调研数据 | 仅生成主题相关插图/图标，预留真实图表区；精确图表另外制作 | 假条形比例、假坐标、虚构引语 | supporting research illustrations, space for editable charts, no fabricated statistical proportions |
| 用户画像 | 用服装、工具、姿态说明角色；预留角色、痛点、需求；按主辅权重制作；标记证据状态 | 虚构履历、刻板印象、重复完整旅程 | compact persona, clear role cues, no invented biographical details |
| 用户旅程 | 阶段按确认顺序，简洁连续路径；行为/问题/机会留白对齐；编号与重点阶段一致 | 断裂、错序、所有节点高亮、复杂漫画 | ordered stages, continuous path, simplified action cues, critical stage emphasis |
| 故事板 | 连续人物产品与事件；起因、压力、冲突、后果、继续；变化镜头；每幕配文留白 | 每幕同姿势、身份漂移、对白、小字、提前虚构方案 | continuous scenario, same character and product, varied framing, cause and consequence, blank captions |
| 设计目标 | 研究收束为方向和范围；少量图形；不提前说明未定结构 | 空泛口号、未验证性能承诺 | research-to-design synthesis, scoped objectives, no unverified claims |
| 产品展示 | 忠实于已确认形态、材质、比例；明确视角；场景说明尺度 | 擅自改设计、多余部件、随机品牌 | faithful product presentation, preserve geometry and materials |
| 结构原理 | 依据结构资料选择爆炸/剖面/序列；连接与运动逻辑一致；标注留空 | 虚构连接、结构矛盾、随机尺寸 | reference-based structure illustration, consistent components and connections |
| 验证 | 区分已实施与计划；展示测试条件/装置；真实结果用工具排入 | 假曲线、计划冒充实测、对照条件不同 | clear test setup, controlled variables, no fabricated results |
| 文创系列 | 保持主题、文化原型与系列一致；包装、三视图相互对应 | 文化乱搭、错误原型、效果图冒充刀模 | coherent cultural series, faithful reference features, consistent packaging views |

## 专项核查
- 多选题说明基数及多选口径；百分比不要求总和100%。比例条必须与数字对应。
- 画像不根据插画给人物编造年龄、收入或引语。非目标人群问卷不能直接证明专业人群画像。
- 旅程是流程定位，故事板是具体事件；两者允许呼应，不重复完整信息。
- 爆炸图的装配逻辑、三视图的对应关系通过原设计校核；生成图不是工程验证。
- 新设计探索与已确认产品表达分开；用户只要求渲染时不要替其重新设计。

## 1.1 真实展板案例引出的专项检查
- **机械轮组**：参考实测CAD/STL/Rhino模型优先决定可核实的外形、分段轮缘、开孔和连接；效果图不能用来虚构遮挡机构。保持不同模块、不同视角轮组来自同一个可核实的设计版本；无法保证时标待核实。
- **装配与缓冲**：区分上承托面/下承载底盘/缓冲连接的位置关系；仅表现已确认的结构，禁止靠机械装饰填充空缺。爆炸图须能对应拆分前后，未知内部机构不能补为已确定机械方案。
- **故事板与旅程**：旅程说明过程阶段，故事板说明一个具体事件的因果；保留角色与物件连续性，用户没有确认的“成功越障”不能插入受阻画面。
- **科学动作序列**：把文献原图、模型演示、AI概念解释分别注明，严格遵循真实资料动作与条件；门槛凸起、地面缝隙、线缆槽等不得混为同一情境。
- **调研统计**：记录样本、有效样本、分母与多选基数；没有依据的数据、图表比例、百分比不能由生成模型补全。
- **文创与包装**：真实文化原型需可回查；盲盒、礼盒、角色三视图要有跨模块一致的确认形态，技术刀模由准确尺寸/结构工具制作，不能把效果图当成刀模。
- **局部替换**：已确认文字、数字、人物数量、故事顺序、装饰与画幅默认为冻结（除非当前任务明确改动）；比对原图，不以“整体更美观”接受非目标区变化。
参考图逐图权限见 `reference-control.md`，提示词分类见 `prompt-schema.md`。
