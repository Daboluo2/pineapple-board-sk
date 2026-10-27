# 菠萝展板sk · 1.1.2

展板制作与自由编辑排版插件。包含技能 `pineapple-board-sk`，以及自包含网页编辑器、生成脚本与参考规则。

## 使用
安装后选择菠萝展板sk，提供计划书、现有素材、项目要求及成品尺寸。示例：“根据我的计划书做一张 A3 竖版展板，先对齐要求与视觉偏好。”也可调用 `$pineapple-board-sk`。

制作过程按阶段确认：①接收与盘点；②内容与证据整理；③页面规划；④视觉系统；⑤母板与素材计划；⑥模块制作与审查；⑦最终排版适配；⑧输出与验收。

编辑网页可下载到本地浏览器打开。一个文件可包含多页，支持拖动绘制八种形状，编辑文字和图片，管理图层与编组，也可撤销重做、保存网页、导出完整布局 JSON 或 SVG，以及打印。单击画布不会创建形状。可靠备份需保存 HTML 或导出完整 JSON，浏览器暂存不替代备份。

技能使用宿主环境提供的文件、代码执行与生图能力；未提供相应能力时明确限制，不承诺所有客户端均能生图或输出文件。浏览器打印和 SVG 导出不等于专业印前 PDF 验证。请以项目或印厂要求验收尺寸、字体、分辨率和色彩。

## 下载与安装

从本仓库的 [v1.1.2 Release](https://github.com/Daboluo2/pineapple-board-sk/releases/tag/v1.1.2) 下载 `pineapple-board-sk-1.1.2.zip`。解压后按下方步骤安装。

### 在 Codex 中手动安装 Skill

1. 解压安装包。
2. 将其中的 `skills/pineapple-board-sk` 整个文件夹复制到用户目录的 `.agents/skills/` 下；Windows 对应 `%USERPROFILE%\.agents\skills\pineapple-board-sk\`。没有父目录时先创建，最终应能找到 `pineapple-board-sk/SKILL.md`。
3. 若已有同名技能，先备份旧版本，再替换；不要保留两份同名安装。
4. 在新聊天中查看技能是否可用，输入 `$pineapple-board-sk`，或要求使用菠萝展板技能制作展板。

也可只为某个项目安装：复制到该项目的 `.agents/skills/pineapple-board-sk/`。此方式安装的是 Skill，不保证在插件目录出现独立插件卡片。

安装目录见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

### 生成离线编辑网页

安装包包含网页模板和 Python 构建脚本，不包含已生成的独立编辑器。可让具备文件和代码执行能力的助手根据已确认布局生成网页，也可在解压后的包根目录运行：

```sh
python -X utf8 skills/pineapple-board-sk/scripts/build_editor.py project.json board.html
```

需要 Python 3，无需额外 Python 依赖。`project.json` 为布局数据，格式见 [可编辑排版说明](skills/pineapple-board-sk/references/editable-layout.md)。生成后用浏览器打开 `board.html`，备份时保存网页或导出完整布局 JSON。

## 发布渠道

本仓库用于 GitHub 源码分发和版本安装包下载；发布 GitHub Release 不等于通过 OpenAI 审核或上架官方插件目录。

## 1.1.2 更新

- 离线可编辑展板工作台：形状按下拖动预览、松开创建，单击画布不创建。
- 同文件多页管理、图层与编组、文字和图片编辑。
- 支持旧版单页 JSON 导入，以及 HTML 保存、JSON/SVG 导出与浏览器打印。
- 延续八步工作流、排版原则、参考图权限与逐图 Prompt 预审。

完整版本记录见 [CHANGELOG.md](CHANGELOG.md)。

## 逐图Prompt预审（1.1补充）
所有实际图像生成与编辑任务（包括视觉母版）在调用 image/image_gen 等工具之前，必须先以文字展示参考图清单及正面、负面、英文补充提示词，并等待用户对本次Prompt明确确认。确认执行大纲、版面尺寸、风格或阶段计划不等于确认生图Prompt；批量操作仅在逐套Prompt先行展示且该批次获得确认时可执行。
