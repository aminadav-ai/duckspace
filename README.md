# 🦆 DuckSpace.org - MicroDuck .ONNX Skill Hub & 3D Home Physics Lab

[![Launch 3D Lab](https://img.shields.io/badge/Launch_3D_Lab-DuckSpace.org-00aeec?style=for-the-badge)](https://duckspace.org)
[![中文版入口](https://img.shields.io/badge/%E4%B8%AD%E6%96%87%E7%89%88-DuckSpace.org%2F%3Flang%3Dzh-fb7299?style=for-the-badge)](https://duckspace.org/?lang=zh)
[![Русская версия](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B0%D1%8F_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F-DuckSpace.org%2F%3Flang%3Dru-7c3aed?style=for-the-badge)](https://duckspace.org/?lang=ru)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-10b981?style=for-the-badge)](./LICENSE)

**Live Platform:** [https://duckspace.org](https://duckspace.org)  
**Languages:** [中文说明](#-中文说明-microduck-技能广场与-3d-家庭物理实验室) | [English](#-english-microduck-onnx-skill-hub--3d-lab) | [На русском](#-на-русском-каталог-навыков-onnx-и-3d-лаборатория-microduck)

---

## 🇨🇳 中文说明：MicroDuck 技能广场与 3D 家庭物理实验室

👉 **立即在线体验（浏览器免安装直玩）：[https://duckspace.org/?lang=zh](https://duckspace.org/?lang=zh)**

**DuckSpace.org** 是专为 **MicroDuck / Open Duck Mini (BDX)** 双足机器人打造的在线 `.ONNX` 步态技能广场与浏览器 3D 物理测试间（基于 **MuJoCo WebAssembly 50Hz** 与 **ONNX Runtime Web**）。

### 核心功能
1. **1楼（底层步态与舵机物理仿真）**：
   * 支持 **飞特舵机 Feetech HD-1910 / HL-2915**、**Feetech STS3215** 以及 **Dynamixel XL330-M288** 硬件配置与齿轮回差仿真。
   * 内置家庭真实障碍环境：22mm 长毛地毯、拖鞋、扫地机器人、充电桩、橘猫与玩具球。
   * 点击任意技能卡片上的 **「▶ 在 3D 房间中运行此 .ONNX」** 即可直接在浏览器里运行，按 **空格键 `Space`** 随时激活或重跑策略。
2. **2楼（AI 自主导航与智能大脑）**：
   * 在线体验防跌落 SLAM 导航、视觉语义巡航、逗猫陪伴追踪、离线语音交互（SenseVoice + YOLO/Qwen）与自动回充。
3. **支持开发者上传 `.ONNX` 与双视频对比**：
   * 在网页顶部点击 **「📤 投稿 .ONNX / 录制视频」**，即可上传自己训练的 `.onnx` 步态文件，并同时附带 **仿真视频 + 真机实拍视频** 供社区对比评分。
   * 网站内置多语言 AI 自动互译（中 / 俄 / 英），全球开发者留言与卡片说明自动互通。

---

## 🌍 English: MicroDuck .ONNX Skill Hub & 3D Lab

👉 **Launch Interactive 3D Lab in Browser: [https://duckspace.org/?lang=en](https://duckspace.org/?lang=en)**

**DuckSpace.org** is an interactive `.ONNX` policy hub and browser-based 3D apartment physics benchmark for **MicroDuck / Open Duck Mini (BDX)** bipedal robots, running **MuJoCo WASM at 50 Hz** directly in the browser without installing Python or Isaac Lab.

### Key Features
* **1st Floor - Locomotion & Servo Profiles:** Test `.onnx` walking, jumping, somersault, and roller-skating policies across **Dynamixel XL330-M288**, **Feetech HD-1910 / HL-2915**, and **Feetech STS3215** profiles on 22mm thick carpet, house slippers, a moving robot vacuum, and an interactive ginger cat.
* **2nd Floor - Autonomous AI Brains:** Test high-level navigation, cliff-guard SLAM, VLM semantic exploration, pet companion tracking, and auto-docking reflexes on top of low-level `.ONNX` locomotion controllers.
* **Dual-Video Comparison & Community Hub:** Upload your `.onnx` checkpoint alongside both **3D Simulation** and **Real Robot** `.mp4`/`.webm` clips, with automatic trilingual translation (`EN` / `中文` / `RU`).

---

## 🇷🇺 На русском: Каталог навыков .ONNX и 3D-лаборатория MicroDuck

👉 **Открыть витрину и 3D-комнату: [https://duckspace.org/?lang=ru](https://duckspace.org/?lang=ru)**

**DuckSpace.org** - интерактивный каталог `.ONNX`-навыков, видео реплик и 3D-квартира (MuJoCo WASM 50 Гц) для двуногих роботов-уток **MicroDuck / Open Duck Mini (BDX)**.

### Возможности платформы
* **1-й этаж (походки, трюки и профили сервоприводов):** тестирование `.onnx`-моделей на профилях **Dynamixel XL330-M288**, **Feetech HD-1910 / HL-2915** и **Feetech STS3215** в 3D-квартире с высоким ворсом ковра (до 22 мм), тапками, роботом-пылесосом, зарядной станцией и рыжим котом. Клавиша **Пробел (`Space`)** активирует выбранный навык.
* **2-й этаж (автономный ИИ-мозг):** тестирование SLAM-навигации, защиты от падения со ступенек, следования за котом, голосового управления и автопарковки на зарядную док-станцию.
* **Загрузка своих `.ONNX` и парных видео (Симуляция + Реальная утка):** любой разработчик может загрузить свой `.onnx`-файл и прикрепить два видео для наглядного сравнения, а встроенный ИИ автоматически переводит описания и комментарии на русский, китайский и английский языки.

---

## 📐 `.ONNX` Policy Tensor Specification (50 Hz)

To run in the **DuckSpace.org** 3D apartment, exported `.onnx` checkpoints use the standard MicroDuck `61D -> 14D` observation/action interface at **50 Hz** (`timestep = 0.005s`, `decimation = 4`):

| Tensor | Shape | Type | Description |
| :--- | :--- | :--- | :--- |
| **Input (`obs`)** | `[1, 61]` | `float32` | `[base_ang_vel(3), projected_gravity(3), joint_pos(14), joint_vel(14), last_action(14), command(13)]` |
| **Output (`act`)** | `[1, 14]` | `float32` | Target joint position offsets (`action_scale` applied at 50 Hz) |

### 14-DOF Joint Order
1. `left_hip_yaw`
2. `left_hip_roll`
3. `left_hip_pitch`
4. `left_knee`
5. `left_ankle`
6. `neck_pitch`
7. `head_pitch`
8. `head_yaw`
9. `head_roll`
10. `right_hip_yaw`
11. `right_hip_roll`
12. `right_hip_pitch`
13. `right_knee`
14. `right_ankle`

### Validate Your `.ONNX` Locally Before Uploading
You can verify any trained `.onnx` checkpoint with our helper script:
```bash
pip install onnxruntime numpy
python3 examples/validate_onnx.py policies/BEST_alpha_walking.onnx
```

---

## 📦 Reference `.ONNX` Policies in [`./policies`](./policies)

| File | Category | Servo Profile | Description |
| :--- | :--- | :--- | :--- |
| [`BEST_alpha_walking.onnx`](./policies/BEST_alpha_walking.onnx) | Carpet Walk | `XL330` / `HD1910` | Baseline omnidirectional walking policy |
| [`rough-walk-g.onnx`](./policies/rough-walk-g.onnx) | Rough Terrain | `XL330` / `HD1910` | High-clearance rough terrain and thick rug walker |
| [`happy-hop.onnx`](./policies/happy-hop.onnx) | Hop / Jump | `XL330` | Happy Hop bipedal hopping gait |
| [`kissqy-hd1910-roulade.onnx`](./policies/kissqy-hd1910-roulade.onnx) | Trick / Roll | `HD1910` | Forward somersault roll & recovery |
| [`kissqy-hd1910-ground-pick.onnx`](./policies/kissqy-hd1910-ground-pick.onnx) | Trick / Crouch | `HD1910` | Deep ground pick / bow maneuver |
| [`duckbuddy-walk.onnx`](./policies/duckbuddy-walk.onnx) | Floor 2 AI Brain | `HL2915` | Low-level locomotion controller for autonomous AI brain |

---

## 🙏 Credits & Open-Source Ecosystem Attribution

* **Pollen Robotics & Hugging Face:** [pollen-robotics/microduck](https://github.com/pollen-robotics/microduck) & [pollen-robotics/microduck_rl](https://github.com/pollen-robotics/microduck_rl) (Apache License 2.0)
* **Chinese Feetech HD-1910 Community Replica:** [fanhao375/microduck-replica](https://github.com/fanhao375/microduck-replica)
* **R17 Firmware & Single-Leg Balance:** [kissqy/Microduck-kissqy](https://github.com/kissqy/Microduck-kissqy)
* **DuckBuddy Voice + Vision AI Brain:** [Animan-AI/DuckBuddy](https://github.com/Animan-AI/DuckBuddy)
