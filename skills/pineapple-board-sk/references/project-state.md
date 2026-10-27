# 项目记录模板

把实例保存在对应项目，依照当前环境的持久保存方式处理；有文件工具时实际保存，没有时输出可复制记录并说明未持久保存。
不要依赖不存在的持久记忆；项目切换时不混用颜色、资料和状态。

```yaml
project_name: ''
execution_mode: prompt_only  # image_generation / layout_file
confirmation_mode: checkpoints # full_execution
current_stage: ''
next_action: ''
requirements_alignment:
  summary: ''
  confirmed: false
  autonomous_authorization: ''
visual_preferences:
  asked: false
  existing_requirements: []
  chosen_direction: ''
  confirmed: false
output_spec:
  size_mm: []
  orientation: ''
  pages: null
  format: ''
  bleed_mm: null
  color_requirement: ''
visual_consensus:
  version: 1
  references: []
  background: ''
  primary: ''
  secondary: ''
  accent: ''
  accent_meaning: ''
  image_style: ''
  type_hierarchy: ''
  lines: ''
  decoration_source: ''
  forbidden_styles: []
  framing: no_placeholder_boxes
  ai_text: no_small_text
layout_reference:
  path: ''
  editable_html_path: ''
  user_edited_version: ''
  confirmed: false
visual_master:
  path: ''
  version: 1
  visual_quality_reviewed: false
  theme_background: ''
  decorative_graphics: ''
  decorative_lines: ''
  confirmed: false
boards: []
modules:
  - id: ''
    purpose: ''
    board: ''
    position: ''
    size_mm: []
    aspect_ratio: ''
    visual_weight: ''
    image_area_mm: []
    image_aspect_ratio: ''
    text_area_mm: []
    text_position: ''
    copy_draft: ''
    character_count: null
    caption_count: null
    font_size_pt: null
    line_spacing: null
    text_fit_verified: false
    image_fit_verified: false
    text_space: ''
    status: pending_creation
    # pending_review / confirmed / temporarily_accepted / pending_adaptation / complete
    asset_version: ''
    asset_path: ''
    evidence_status: ''
    unresolved: []
evidence:
  - claim: ''
    source: ''
    denominator: null
    calculation: ''
    status: unverified # verified / hypothesis / target / placeholder
editor:
  html_path: ''
  editing_verified: false
  save_reload_verified: false
  print_verified: false
open_issues: []
confirmed_decisions: []
```

## 更新与恢复
主要决策或素材变更后更新记录。保留版本路径，避免覆盖唯一原稿。
恢复时验证文件实际存在；路径失效先寻找对应资料，不编造读取成功。
发现新资料与旧记录冲突，以当前权威资料为准，说明影响并更新。
回退时选择已确认版本；重大风格修改升级视觉共识版本，列出受影响模块。

## 分开记录验收
记录几何布局确认、母版美感确认、文字容纳、图片适配和最终输出；不因一种通过而标全部完成。案例验证不自动改成成品制作。

## 1.1 项目状态扩展（保持旧字段可用）
下面字段作为可选扩展并入对应项目的YAML/JSON，不要求旧项目立刻补齐。不能将其误当成新的全局默认视觉偏好。

```yaml
skill_version: '1.1.0'
constraint_scopes:
  global_policy: []      # 仅Skill行为原则
  project_confirmed: [] # 当前项目已确认设计事实
  page_confirmed: []    # 仅指定展板
  task_only: []         # 本次操作完成后不自动继承
reference_assets:
  - filename: ''
    version: ''
    purpose: ''          # geometry / appearance / layout / visual_style / scene / evidence
    authority_for: []
    forbidden_uses: []
    status: pending_verification
    source: ''
version_control:
  base_version: ''
  working_version: ''
  last_confirmed_version: ''
  frozen_regions: []
  editable_regions: []
stage_checkpoints:
  - stage: 1
    status: pending # pending / presented / confirmed / failed
    evidence: ''
quality_gates:
  visual: untested
  evidence: untested
  structure: untested
  layout: untested
  text: untested
  edit_fidelity: untested
  editor: untested
  export: untested
```

**状态更新触发**：新增或替换参考图、当前指令覆盖已确认约束、完成模块生成、完成局部修复、母版/布局版本更新、验收失败与回退。记录修改对象和影响范围，避免无关阶段重复写回所有状态。全局原则与局部任务条件不得混存。用户确认某个模块不等于整张展板或产品结构已完成验收。
