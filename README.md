# Codex 科研云环境

用于 Python 科学计算、论文 PDF/Word/Excel 处理和无人艇控制原型仿真。
本仓库只提供通用工具配置及合成模型检查，不包含论文、实验数据、密钥或个人信息。

## 环境安装

选择 Python 3.12。主要依赖版本已固定，仓库根目录执行：

```bash
bash setup.sh
```

脚本建立仓库内 `.venv`，安装依赖，运行数值与文件读写检查，执行 `pip check`，
并将实际版本写入 `requirements.resolved.txt`。后续使用 `.venv/bin/python`。
安装不需要 API 密钥，也不依赖本机 SSH 密钥。

## 在 Codex 中创建

按照[官方云环境指南](https://learn.chatgpt.com/docs/environments/cloud-environments)：

1. 登录 ChatGPT，在新任务选择 `Work in > Cloud > Select environment > Create environment`，
   或进入 `Settings > Codex Cloud > Environments > Create environment`。
2. 选择仓库 `biancatticleity-gif/codex_cloud_space`；未连接 GitHub 时完成官方授权。
3. 环境命名建议为 `research-usv-python`，选择 `Get started`。
4. 请 Codex 执行根目录 `bash setup.sh`，检查全部通过后保存并 `Publish`。
5. 出现 `Environment published` 后，在新云任务中再次执行：

```bash
.venv/bin/python verify_environment.py
.venv/bin/python -m pip check
```

输出 `PASS` 且无依赖冲突才算云端验收通过。提交配置本身不等于发布云环境。
若界面是旧版 Cloud (Legacy)，将 `bash setup.sh` 填入安装脚本字段；其联网与 secrets 行为不同，
请遵循对应设置页面，勿混用新版个人 vault 说明。

## 工具与检查

NumPy、SciPy、Pandas、SymPy、Matplotlib、python-control、PyMuPDF、pypdf、python-docx、
openpyxl、pytest、ipykernel、nbformat。

`verify_environment.py` 检查模块导入、一阶艏摇角速度模型的积分解与解析解一致、
传递函数稳定性、无界面 PNG 导出与 PDF 读写。
示例是合成的一阶模型，不是已校准的无人艇动力学模型。

GitHub Actions 中的 `Validate research environment` 工作流在 Ubuntu 上执行完整安装和验收。
它验证 Linux 安装脚本与依赖；通过该检查仍需在实际 Codex 云任务中完成环境验收。

## 文稿规则

遵守 `AGENTS.md`：正文宋体，标题黑体，英文与数字 Times New Roman，公式 Cambria Math；
清理标题的主题字体残留。Linux 云环境可能没有这些字体，应检查实际字体可用性。
文件中的字体声明与最终渲染是否使用该字体需分别验证。

## 范围

当前不包含 MATLAB/Simulink、ROS、GPU、OCR 或完整无人艇模型。按后续项目需要增补。
云任务中的文件、字体和技能以该云环境为准；本机登录、文件及个人技能不会自动转移。
安装依赖需可访问 PyPI 包索引和文件分发域名；联网策略由环境设置控制。
