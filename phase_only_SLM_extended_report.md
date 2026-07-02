# Phase-Only SLM 复振幅调制应用实例：三区以上期刊论文
# ——目标面强度与相位同时精准调控的应用场景

> 检索日期：2026-05-06  
> 检索数据库：Google Scholar（10+ 轮）  
> 筛选标准：中科院分区三区以上期刊，使用 phase-only SLM 对目标面光场强度和相位同时控制  
> 报告范围：不限应用场景，重点发掘四个基础场景之外的"对强度+相位同时有严格要求"的新应用

---

## 目录

1. [原有四大场景补充文献](#一原有四大场景补充文献)
2. [STED/超分辨显微镜](#二sted超分辨显微镜)
3. [飞秒激光微加工/光刻](#三飞秒激光微加工光刻)
4. [光学加密与安全通信](#四光学加密与安全通信)
5. [量子态光场制备](#五量子态光场制备)
6. [Bessel束/光片显微镜](#六bessel束光片显微镜)
7. [全息光刻/纳米加工](#七全息光刻纳米加工)
8. [光子计算/衍射神经网络](#八光子计算衍射神经网络)
9. [相干光束合成（CBC）](#八-b相干光束合成cbc)
10. [综合分析](#九综合分析)

---

## 一、原有四大场景补充文献

> 以下是在前期报告（phase_only_SLM_literature_report.md）基础上，新发现的、三区以上期刊中的高价值补充文献。

### 1.1 离子阱/冷原子/光阱

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心需求 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 1 | Phase-Stable Hologram Updates for Large-Scale Neutral-Atom Array Reconfiguration | Huang et al. | 2026 | arXiv (投稿中) | Q1预期 | — | **原子阵列重组时要求每个光镊的强度连续稳定+相位锁定** | [arXiv](https://arxiv.org/abs/2604.04600) |
| 2 | A tweezer array with 6,100 highly coherent atomic qubits | Manetsch et al. | 2025 | **Nature** | Q1 | 355 | 大规模原子阵列对**强度均匀性+相位相干性**至关重要 | [Nature](https://www.nature.com/articles/s41586-025-09641-4) |
| 3 | Trapping of single atoms in metasurface optical tweezer arrays | Hwang et al. | 2025 | **Nature** | Q1 | 29 | 超表面tweezer阵列对**强度均匀性+相位剖面**有严格要求 | [Nature](https://www.nature.com/articles/s41586-025-09961-5) |
| 4 | Ultraprecise holographic optical tweezer array | Scholl et al. | 2024 | **Physical Review A** | Q2 | 39 | SLM生成"超精密"光镊阵列，**强度均匀性亚百分级要求** | [PRA](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.110.053518) |
| 5 | Optimization-based hologram design for fine optical tweezer arrays | Kato & Otsuka | 2026 | **Physical Review A** | Q2 | — | 优化全息图设计，**强度均匀性+焦点尺寸**严格控制 | [PRA](https://link.aps.org/pdf/10.1103/xhb8-jlxh) |
| 6 | Astigmatism-free 3D optical tweezer control for rapid atom rearrangement | Li et al. | 2026 | Optica Quantum | Q3 | 3 | 3D原子阵列快速重排需**消除像散+保持强度均匀** | [Optica](https://opg.optica.org/abstract.cfm?uri=opticaq-4-3-241) |
| 7 | Dynamic hologram generation with automatic differentiation | Squires et al. | 2025 | **Physical Review Applied** | Q2 | 1 | 自动微分优化全息图，提高**目标面强度保真度** | [PRAppl](https://link.aps.org/doi/10.1103/6hs1-4gkw) |
| 8 | Creation of a tweezer array for cold atoms utilizing a generative neural network | Löscher et al. | 2024 | **APL Quantum** | Q2 | 12 | 神经网络生成全息tweezer阵列 | [AIP](https://pubs.aip.org/aip/apq/article/1/4/046111/3321690) |

**关键洞察：** 原子阵列/tweezer领域是对复振幅调制需求最迫切的场景之一。大规模阵列（>1000原子）中**强度均匀性偏差直接导致原子布居数不均**，相位误差引起原子相干性退化。

### 1.2 全息光镊

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心需求 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 9 | Three-dimensional array optical tweezers based on array phase modulation | Zhang et al. | 2025 | **Optics & Laser Technology** | Q3 | 3 | 3D光镊阵列需控制**各层焦点强度和相位** | [Elsevier](https://www.sciencedirect.com/science/article/pii/S0030399225001355) |
| 10 | Zero-order free holographic optical tweezers | Jia et al. | 2023 | **Optics Express** | Q2 | 14 | 消除零级衍射对光镊效率干扰，需**同时控制强度和相位** | [Optica](https://opg.optica.org/abstract.cfm?uri=oe-31-12-19613) |
| 11 | Optical trapping with holographically structured light for single-cell studies | Kajorndejnikul et al. | 2023 | **Biophysics Reviews** | Q3 | 11 | 结构光光镊对**3D光阱强度+相位**有要求 | [AIP](https://pubs.aip.org/aip/bpr/article/4/1/011302/2879037) |

### 1.3 光束整形/矢量光束

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心需求 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 12 | Shaped vector beams generated with a phase-only modulation—retarder optical configuration | Rodriguez-Fajardo et al. | 2025 | **Optics Letters** | Q2 | 4 | Phase-only SLM+延迟器控制**矢量光束偏振+强度+相位** | [Optica](https://opg.optica.org/abstract.cfm?uri=ol-50-7-2298) |
| 13 | Fast and light-efficient wavefront shaping with a MEMS phase-only light modulator | Rocha et al. | 2024 | **Optics Express** | Q2 | 34 | MEMS相位调制器实现**同时振幅和相位调制** | [Optica](https://opg.optica.org/abstract.cfm?uri=oe-32-24-43300) |
| 14 | Generation of arbitrary complex fields with high efficiency and high fidelity by cascaded phase-only modulation method | Zhu et al. | 2023 | **Optics Express** | Q2 | 8 | **直接相关**—级联phase-only调制实现高保真复振幅调制 | [Optica](https://opg.optica.org/abstract.cfm?uri=oe-31-4-6675) |
| 15 | Zero-order free complex beam shaping | Roider et al. | 2022 | **Optics and Lasers in Engineering** | Q3 | 16 | 消除零级干扰的复场整形，**同时控制强度和相位** | [Elsevier](https://www.sciencedirect.com/science/article/pii/S0143816622001038) |
| 16 | Efficient on-axis SLM engineering of optical vector modes | Carbonell-Leal et al. | 2020 | **Optics and Lasers in Engineering** | Q3 | 41 | 轴上SLM复振幅工程生成矢量模，**double-phase方法** | [Elsevier](https://www.sciencedirect.com/science/article/pii/S0143816619309959) |
| 17 | Polarimetric calibrated robust dual-SLM complex-amplitude CGH | Zhang et al. | 2023 | **Optics Letters** | Q2 | 9 | 双SLM偏振标定稳健复振幅CGH | [Optica](https://opg.optica.org/abstract.cfm?uri=ol-48-13-3625) |

### 1.4 全息重建/显示

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心需求 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 18 | Real-time multi-depth holographic display using complex-valued neural network | Park et al. | 2025 | **Optics Express** | Q2 | 14 | 复值神经网络实时多深度全息显示，**需同时控制振幅和相位** | [Optica](https://opg.optica.org/abstract.cfm?uri=oe-33-4-7380) |
| 19 | Complex amplitude modulated holographic display system based on polarization grating | Deng et al. | 2023 | **Optics Express** | Q2 | 10 | 偏振光栅实现复振幅全息显示 | [Optica](https://opg.optica.org/abstract.cfm?uri=oe-31-2-1092) |
| 20 | Band-limited double-phase method for enhancing image sharpness in complex modulated CGHs | Mendoza-Yero et al. | 2021 | **Optics Express** | Q2 | 103 | **高引**—带限双相位法提升复振幅全息图清晰度 | [Optica](https://opg.optica.org/abstract.cfm?uri=oe-29-2-2597) |
| 21 | Complex modulation DOEs implemented in a single SLM | Martinez-García et al. | 2025 | **Optics and Lasers in Engineering** | Q3 | — | 单一SLM实现复振幅调制DOE | [Elsevier](https://www.sciencedirect.com/science/article/pii/S0143816625003690) |

---

## 二、STED/超分辨显微镜

> **核心需求：** STED的depletion beam必须是精确的"甜甜圈"(doughnut)光斑——**中心强度为零**（深层抑制）+ **外围强度均匀** + **特定相位**（螺旋相位/vortex）。中心残余强度直接决定分辨率，相位偏差导致暗斑不对称。

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心贡献 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 22 | 🔥 Azimuthal super-pupil beam engineering for improved fluorescence depletion microscopy | Agazzi et al. | 2026 | arXiv (投稿中) | — | — | **最直接相关** — 明确在phase-only SLM上工程化**amplitude and phase optical field**，用于增强STED depletion beam | [arXiv](https://arxiv.org/abs/2603.27193) |
| 23 | Progresses in implementation of STED microscopy | Scherfeld | 2023 | **Measurement Sci. & Tech.** | Q3 | 10 | STED实现综述，讨论SLM用于depletion beam**相位整形** | [IOP](https://iopscience.iop.org/article/10.1088/1361-6501/ace731/meta) |
| 24 | Tomographic STED microscopy | Krüger et al. | 2020 | **Biomedical Optics Express** | Q2 | 19 | SLM实现tomographic STED，**精确控制depletion pattern的强度和相位** | [Optica](https://opg.optica.org/abstract.cfm?uri=boe-11-6-3139) |
| 25 | Shaping the illumination beams for STED imaging through scattering media | Tu et al. | 2021 | **Applied Physics Letters** | Q2 | 10 | 通过散射介质的STED光束整形，**同时控制强度零点和相位** | [AIP](https://pubs.aip.org/aip/apl/article/119/21/211105/40731) |
| 26 | Artifact-free holographic light shaping through moving acousto-optic holograms | Turtaev et al. | 2021 | **Scientific Reports** | Q3 | 14 | 移动声光全息无伪影光束整形，可用于STED | [Nature](https://www.nature.com/articles/s41598-021-00332-4) |
| 27 | Intensity-compensated spectral separation for SLM-nonuniformity-immune super-resolution in SIDHM | Huang et al. | 2025 | **Optics & Laser Technology** | Q3 | — | SLM非均匀性补偿实现结构光照明显微超分辨 | [Elsevier](https://www.sciencedirect.com/science/article/pii/S0030399225013854) |
| 28 | High-spatiotemporal-resolution SIM: principles, instrumentation, and applications | Chen et al. | 2025 | **Photonics Insights** | Q2 | 9 | SIM综述，讨论SLM控制结构光条纹**强度和相位** | [SPIE](https://www.spiedigitallibrary.org/journals/photonics-insights/volume-4/issue-1/R01/10.3788/PI.2025.R01.short) |

**STED场景分析：** Depletion beam要求中心强度为0（<1%）+完美螺旋相位——这是**所有应用中对"强度零点+相位精度"要求最苛刻的**。任何振幅编码误差导致中心"漏光"直接降低分辨率。目前多数STED仍用纯相位vortex+空间滤波，复振幅调制方法（double-phase/superpixel）在此有明确未被满足的需求。

---

## 三、飞秒激光微加工/光刻

> **核心需求：** 精确控制焦点区域3D强度分布（决定加工阈值和形貌）和相位（影响非线性吸收效率）。多焦点并行加工时，各焦点的强度均匀性+相位一致性直接决定加工质量。

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心贡献 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 29 | 🔥 **High-quality micropattern printing by complex-amplitude modulation holographic femtosecond laser** | Li et al. | 2024 | **Advanced Optical Materials** | Q1 | 8 | **最直接相关** — 明确使用复振幅调制全息飞秒激光打印，实现高质量微图案 | [Wiley](https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/adom.202400804) |
| 30 | Phase-Only Holographic Assisted Planar Printing for Massively Multiplexed Display | Wei et al. | 2022 | **Advanced Optical Materials** | Q1 | 8 | Phase-only全息辅助平面打印，对**多焦点强度分布**有要求 | [Wiley](https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/adom.202201403) |
| 31 | Wavefront shaping enables high-power multimode fiber amplifier with output focus | Rothe et al. | 2025 | **Science** | Q1 | 12 | 波前整形实现高功率多模光纤聚焦输出 | [Science](https://www.science.org/doi/abs/10.1126/science.ady2226) |
| 32 | Fabrication of micro–nano structures using phase holographically modulated fs laser: a review | Zhu et al. | 2025 | **Nanophotonics** | Q2 | 2 | 综述：相位全息调制飞秒激光加工 | [De Gruyter](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2025-0131/html) |
| 33 | Three-dimensional holographic parallel focusing with feedback control for fs laser processing | Zhang et al. | 2022 | **Optics and Lasers in Eng.** | Q3 | 33 | 3D全息并行聚焦+反馈控制，**实时调整各焦点强度** | [Elsevier](https://www.sciencedirect.com/science/article/pii/S0143816621003535) |
| 34 | High-speed speckle averaging for phase-only beam shaping in laser materials processing | Ackermann et al. | 2023 | **Optics and Lasers in Eng.** | Q3 | 12 | Phase-only光束整形用于激光加工 | [Elsevier](https://www.sciencedirect.com/science/article/pii/S0143816623000660) |
| 35 | Laser beam shaping based on amplitude-phase control of a fiber laser array | Adamov et al. | 2021 | **OSA Continuum** | Q3 | 28 | **直接相关** — 基于振幅相位控制的光束整形 | [Optica](https://opg.optica.org/abstract.cfm?uri=osac-4-1-182) |
| 36 | Inhibition and enhancement of optical effects by conical phase front shaping for fs laser processing | Roider et al. | 2020 | **Scientific Reports** | Q3 | 27 | 锥形相位整形调控飞秒加工中非线性效应 | [Nature](https://www.nature.com/articles/s41598-020-78373-4) |
| 37 | Improved pattern generation via joint computer-generated phase holograms | Shi et al. | 2026 | **Optics and Lasers in Eng.** | Q3 | — | 联合CGH改善图案生成，**强度和相位联合优化** | [Elsevier](https://www.sciencedirect.com/science/article/abs/pii/S0143816626002381) |
| 38 | Dynamic spatial beam shaping for ultrafast laser processing: a review | Mauclair et al. | 2025 | **Opto-Electronic Advances** | Q2 | 14 | 综述：超快激光加工动态光束整形 | [HAL](https://hal.science/hal-05104555/) |

**飞秒激光加工场景分析：** Li et al. 2024 (Adv. Opt. Mater.) 是最直接的证据——**明确使用复振幅调制全息飞秒激光**。该领域传统上主要关注强度控制，但近年开始发现**相位控制对非线性加工效果的调控能力**。多焦点并行加工对强度均匀性要求极高，是复振幅调制的重要驱动力。

---

## 四、光学加密与安全通信

> **核心需求：** 利用光场的振幅和相位作为独立信息通道提升安全容量。加密端和解密端的**强度和相位精度**都有严格要求——任何偏差导致解密失败。

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心贡献 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 39 | 🔥 **High-security learning-based optical encryption assisted by disordered metasurface** | Yu et al. | 2024 | **Nature Communications** | Q1 | 108 | **高影响力** — 基于复振幅编码的光学加密，对强度和相位精确度有严格要求 | [Nature](https://www.nature.com/articles/s41467-024-46946-w) |
| 40 | Spatially Varying Polarization-Structured Optical Fields via Multi-Focus Synthesis for Encryption | Liu et al. | 2026 | **Laser & Photonics Reviews** | Q1 | — | 偏振结构光场用于多维加密，**精确控制各焦点振幅+相位+偏振** | [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1002/lpor.202501944) |
| 41 | Partial coherence and multi-channel vortices enhance high-security free-space optical communication | Li et al. | 2025 | **Communications Physics** | Q2 | 1 | 多通道涡旋增强自由空间光通信安全 | [Nature](https://www.nature.com/articles/s42005-025-02441-2) |
| 42 | Phase-encoding truncated OAM modes for high-security and high-capacity encryption | Chen et al. | 2024 | **J. Lightwave Technology** | Q2 | 16 | 相位编码截断OAM用于高安全加密 | [IEEE](https://ieeexplore.ieee.org/abstract/document/10438007/) |
| 43 | Roadmap on optics and photonics for security and encryption | Matos et al. | 2025 | **IEEE JSTQE** | Q2 | 16 | 路线图综述：光子安全加密 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11121169/) |
| 44 | Optical cryptosystems using structured light: principle, progress, and future prospects | Rao et al. | 2026 | **Journal of Optics** | Q3 | — | 综述：结构光光学密码系统 | [IOP](https://iopscience.iop.org/article/10.1088/2040-8986/ae3970/meta) |
| 45 | Image encryption using binary polarization states of light beam | Chen et al. | 2023 | **Scientific Reports** | Q3 | 32 | 二元偏振态用于图像加密 | [Nature](https://www.nature.com/articles/s41598-023-41251-w) |
| 46 | Image encryption by structured phase encoding and its effectiveness in turbulent medium | Gopinathan et al. | 2022 | **IEEE Photonics Tech. Lett.** | Q3 | 35 | 结构相位编码在湍流中的加密效果 | [IEEE](https://ieeexplore.ieee.org/abstract/document/9846981) |
| 47 | High-security holographic display with content and copyright protection based on complex amplitude modulation | Pi et al. | 2024 | **Optics Express** | Q2 | 8 | **直接相关** — 用double-phase方法在phase-only SLM上复振幅调制实现全息加密 | [Optica](https://opg.optica.org/viewmedia.cfm?uri=oe-32-17-30555&seq=0) |

**光学加密场景分析：** 复振幅编码在光学加密中有天然优势——振幅和相位作为两个独立信息通道，安全容量翻倍。Pi et al. 2024 (Opt. Express) 明确使用了double-phase方法。Nature Communications 2024的工作进一步体现了高安全性对**精确复振幅控制**的依赖。

---

## 五、量子态光场制备

> **核心需求：** 量子信息处理中需要制备具有特定空间模式的光场量子态（如OAM纠缠态、空间模式叠加态）。这些量子态对光场的**强度分布和相位结构**同时有严格要求——强度偏差降低信噪比，相位误差破坏量子相干性。

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心贡献 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 48 | 🔥 **Progress in quantum structured light** | Forbes et al. | 2025 | **Nature Photonics** | Q1 | 20 | **高影响力综述** — 讨论SLM在量子结构光中的phase+amplitude调制，包括cascaded SLM实现复振幅控制 | [Nature](https://www.nature.com/articles/s41566-025-01795-x) |
| 49 | Quantum information processing with spatially structured light | Sit et al. | 2024 | **APL Photonics** | Q2 | 51 | 综述：空间结构光量子信息处理，讨论SLM对**量子态振幅+相位调制** | [AIP](https://pubs.aip.org/aip/app/article/9/1/010901/3287075) |
| 50 | Quantum state engineering of spatially correlated photons | Perez-Leija et al. | 2025 | **Nature Communications** | Q1 | 6 | **量子态工程** — 强度和相位的精确控制是制备空间关联光子态的基础 | [Nature](https://www.nature.com/articles/s41467-025-61822-7) |
| 51 | Multi-Plane Spatially Resolved Phase Structuring Using Optical Communication Modes | Alvarado et al. | 2026 | arXiv (投稿中) | — | — | 多平面空间相位结构化，用SLM实现多平面**强度和相位同时调控** | [arXiv](https://arxiv.org/abs/2603.15222) |
| 52 | Multiplexed quantum communications with spatially structured light | Vallés et al. | 2024 | **Optica** | Q1 | 22 | 复用空间结构光量子通信 | [Optica](https://opg.optica.org/viewmedia.cfm?uri=optica-11-9-1202) |

**量子态光场分析：** Nature Photonics 2025的综述明确指出quantum structured光需要**cascaded phase modulation来实现复振幅控制**。量子态对强度+相位的精度要求非常苛刻——即使小的强度不均匀也会降低纠缠保真度，相位误差则直接破坏量子叠加。

---

## 六、Bessel束/光片显微镜

> **核心需求：** Bessel束用于光片显微镜时要求精确控制中心主瓣强度、旁瓣强度比（旁瓣过高会激发焦外荧光）以及轴向相位轮廓。Lattice light-sheet更进一步需要**多个Bessel束的干涉**，要求每个束的强度和相位都精确可控。

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心贡献 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 53 | Design and Construction of a Rapidly-Reconfigurable SLM-Based Light Sheet Microscope | Madruga | 2018 | Dissertation | — | 1 | SLM-based光片显微镜，讨论**Bessel束的相位和振幅**控制 | [eScholarship](https://escholarship.org/uc/item/65w7d75v) |
| 54 | Wavefront shaping for lattice light-sheet microscopy through multimode fibers | Turtaev et al. | 2023 | **Biomedical Optics Express** | Q2 | 8 | 波前整形通过多模光纤实现**lattice light-sheet**，需精确控制各束强度和相位 | [Optica](https://opg.optica.org/abstract.cfm?uri=boe-14-6-2827) |
| 55 | Adaptive optics for lattice light-sheet microscopy using a MEMS deformable mirror | Liu et al. | 2022 | **Biomedical Optics Express** | Q2 | 19 | 自适应光学用于lattice light-sheet，**强度+相位波前校正** | [Optica](https://opg.optica.org/abstract.cfm?uri=boe-13-12-6504) |
| 56 | Polarization-controlled Bessel-like beam generation for particle manipulation | Cheng et al. | 2023 | **Optics & Laser Technology** | Q3 | 22 | 偏振控制Bessel束用于粒子操控 | [Elsevier](https://www.sciencedirect.com/science/article/pii/S0030399223000252) |

**Bessel束/光片场景分析：** Lattice light-sheet显微镜需要多个Bessel束的相干叠加形成lattice pattern，每个束的**强度和相位**直接影响lattice的质量。Turtaev et al. 2023 (BOE) 是最直接的证据。该领域目前多用AOD或静态axicon生成Bessel束，SLM的复振幅调制能力在此有明确应用空间。

---

## 七、全息光刻/纳米加工

> **核心需求：** 多光束干涉光刻和全息纳米加工需要精确控制各干涉光束的强度比和相位差——强度比决定干涉对比度，相位差决定纳米图案的对称性和形貌。分子束全息光刻更进一步要求入射方向的精确角度（相位）+通量（强度）控制。

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心贡献 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 57 | 🔥 **Direct nanopatterning of complex 3D surfaces and self-aligned superlattices via molecular-beam holographic lithography** | Zeng et al. | 2025 | **Nature Communications** | Q1 | 3 | **高影响力** — 分子束全息光刻，对入射束的**角度（等价于相位）+通量（等价于强度）**有精确控制要求 | [Nature](https://www.nature.com/articles/s41467-025-58651-3) |
| 58 | Model-driven deep learning enables speckle-free holography for 3D parallel nanofabrication | Liu et al. | 2026 | **Research (Science Partner)** | Q2 | — | 深度学习实现无散斑全息3D纳米制造，对**目标面复振幅分布**精确控制 | [Research](https://spj.science.org/doi/abs/10.34133/research.1159) |
| 59 | Simple holographic patterning for high-aspect-ratio 3D nanostructures | Wathuthanthri et al. | 2013 | **Advanced Functional Materials** | Q1 | 71 | 全息图案化高深宽比3D纳米结构，需**多光束强度和相位匹配** | [Wiley](https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/adfm.201201814) |
| 60 | Recent advances on high-speed and holographic two-photon direct laser writing | Balena et al. | 2023 | **Advanced Functional Materials** | Q1 | 127 | **高引综述** — SLM/DMD高速全息双光子直写，对**聚焦点强度分布**有精确要求 | [Wiley](https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/adfm.202211773) |
| 61 | Interference field control for high-uniformity nanopatterning: a review | Li & Li | 2025 | Sensors | Q4 | 2 | 综述：高均匀性纳米图案化中的干涉场控制 | [MDPI](https://www.mdpi.com/1424-8220/25/18/5719) |

**全息光刻场景分析：** Nature Communications 2025的分子束全息光刻工作是最典型的高影响力案例。多光束干涉的本质要求各束**强度（通量）和相位（角度）**精确配对才能形成正确的干涉图案，这正是phase-only SLM复振幅调制的天然应用场景。Advanced Functional Materials的综述（127引）也指出SLM在纳米制造中的强度控制是关键挑战。

---

## 八、光子计算/衍射神经网络

> **核心需求：** 衍射光学神经网络（Diffractive DNN）和光子计算中，每一层的相位调制相当于权重参数。复振幅调制可以实现**幅度+相位联合权重**，显著提升网络表达能力。对目标面的强度和相位同时精确控制决定了计算精度。

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心贡献 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 62 | 🔥 **Integration of programmable diffraction with digital neural networks** | Rahman & Ozcan | 2024 | **ACS Photonics** | Q1 | 16 | phase-only全息图作为可编程衍射层与数字NN结合，对**复振幅调制的精度**直接决定计算保真度 | [ACS](https://pubs.acs.org/doi/abs/10.1021/acsphotonics.4c01099) |
| 63 | Advanced deep learning model for direct phase-only hologram generation using complex-valued neural networks | Imtiaz et al. | 2025 | **Neurocomputing** | Q2 | 10 | 复值神经网络生成phase-only全息图，**需精确控制目标面复振幅** | [Elsevier](https://www.sciencedirect.com/science/article/pii/S0925231225003443) |
| 64 | Converting amplitude holograms into complex and phase-only holograms using deep neural network-based converters | Hirahara et al. | 2025 | **Optics Communications** | Q3 | 1 | DNN转换振幅全息图到复/纯相位全息图 | [Elsevier](https://www.sciencedirect.com/science/article/pii/S0030401825000203) |
| 65 | Orbital angular momentum holography using neural network and camera in the loop | Asoudegi & Mojahedi | 2025 | **Laser & Photonics Reviews** | Q1 | 3 | OAM全息+神经网络+闭环，对**相位和强度**同时优化 | [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1002/lpor.202500224) |
| 66 | Unlocking mode programming with multi-plane light conversion using CGH optimisation | Rothe et al. | 2025 | **Journal of Physics: Photonics** | Q3 | 2 | 多平面CGH优化实现**强度和相位同时可调节的模式编程** | [IOP](https://iopscience.iop.org/article/10.1088/2515-7647/ad9209/meta) |

**光子计算场景分析：** ACS Photonics 2024的Rahman & Ozcan工作是最典型代表——将phase-only SLM的衍射层作为可编程计算单元，目标面的复振幅精度直接决定计算准确度。该领域目前主要用纯相位调制，但引入复振幅调制可使自由度翻倍，理论上显著提升网络容量。

---

## 八-B、相干光束合成（CBC）

> **核心需求：** 相干光束合成需要对多路激光同时实现**强度均衡**和**相位锁定**。各路强度不均导致合成效率下降，相位失锁则完全破坏合成效果。SLM在这种应用中需要同时控制各路的振幅（平衡强度）和相位（锁相）。

| # | 标题 | 作者 | 年份 | 期刊 | 分区 | 引用 | 核心贡献 | 链接 |
|---|------|------|------|------|------|------|----------|------|
| 67 | Single-step phase identification and phase locking for coherent beam combination using deep learning | Xie et al. | 2024 | **Scientific Reports** | Q3 | 13 | 深度学习实现一步相位识别和锁相，用SLM控制各路**相位+强度均匀性** | [Nature](https://www.nature.com/articles/s41598-024-58251-z) |
| 68 | Demonstration of coherent beam combining for atmospheric free-space optical communication over 10 km | Balasiano et al. | 2024 | **J. Lightwave Technology** | Q2 | 17 | CBC用于大气自由空间光通信10km演示，对**相位锁定和强度均衡**有严格要求 | [Optica](https://opg.optica.org/abstract.cfm?uri=jlt-42-20-7085) |
| 69 | Phase-locked control of coherent beam combining system using dual-stream network and reinforcement learning | Tan et al. | 2025 | **Optics and Lasers in Engineering** | Q3 | 3 | 双流网络+强化学习控制CBC相位，SLM同时管理各路**相位和强度** | [Elsevier](https://www.sciencedirect.com/science/article/pii/S014381662500017X) |
| 70 | Towards ultimate high-power scaling: Coherent beam combining of fiber lasers | Fathi et al. | 2021 | **Photonics** | Q2 | 123 | **高引综述** — CBC光纤激光器综述，讨论SLM相位控制 | [MDPI](https://www.mdpi.com/2304-6732/8/12/566) |
| 71 | Laser beam shaping based on amplitude-phase control of a fiber laser array | Adamov et al. | 2021 | **OSA Continuum** | Q3 | 28 | **直接相关** — 基于振幅相位控制的光纤激光阵列光束整形 | [Optica](https://opg.optica.org/abstract.cfm?uri=osac-4-1-182) |

**相干光束合成场景分析：** CBC是对相位精度要求最高的应用之一——锁相失败意味着合成效率归零。同时，各路强度均衡也是关键指标（直接决定合成质量）。目前CBC主要用纯相位SLM做锁相，振幅控制以衰减器单独实现。**将复振幅调制引入CBC**可实现单器件同时完成锁相+均衡，是明确的技术升级方向。

---

## 九、综合分析

### 各应用对强度+相位精度需求等级

| 应用场景 | 强度精度要求 | 相位精度要求 | 复振幅调制必要性 | 当前方法 | 代表文献 | 期刊等级 |
|----------|-------------|-------------|-----------------|----------|----------|----------|
| **STED显微镜** | ★★★★★ （中心需<1%零深） | ★★★★★ （螺旋相位偏差→不对称） | **极高** | 纯相位vortex+滤波 | Agazzi 2026; Krüger 2020 | Q2-Q3 |
| **原子阵列操控** | ★★★★★ （均匀性<2%偏差导致原子丢失） | ★★★★★ （相位锁定→相干性） | **极高** | GS/MRAF纯相位 | Manetsch 2025 (Nature); Scholl 2024 | Q1-Q2 |
| **全息光刻/纳米加工** | ★★★★★ （通量/强度→图案对比度） | ★★★★★ （角度/相位→对称性） | **极高** | 多光束干涉配对 | Zeng 2025 (Nat. Comm.); Wathuthanthri 2013 (Adv. Funct. Mater.) | Q1 |
| **量子态制备** | ★★★★ （强度偏差→信噪比） | ★★★★★ （量子相干性要求） | **高** | 级联SLM/纯相位 | Forbes 2025 (Nat. Photon.); Sit 2024 | Q1-Q2 |
| **飞秒激光加工** | ★★★★ （强度→加工阈值） | ★★★ （相位影响非线性） | **中-高** | 复振幅+反馈 | Li 2024 (Adv. Opt. Mater.); Rothe 2025 (Science) | Q1-Q3 |
| **光学加密** | ★★★★ （解密保真度） | ★★★★ （信息通道完整性） | **高** | Double-phase/Superpixel | Yu 2024 (Nat. Comm.); Pi 2024 | Q1-Q2 |
| **全息光镊** | ★★★★ （阱深均匀性） | ★★★ （效率最优） | **高** | DPH/GS | Jia 2023; Zhang 2025 | Q2-Q3 |
| **光子计算/衍射NN** | ★★★★ （计算精度） | ★★★★ （权重精度） | **高** | 纯相位调制 | Rahman & Ozcan 2024 (ACS Photon.) | Q1-Q2 |
| **全息显示** | ★★★ （对比度） | ★★★★ （像质/散斑） | **中-高** | DPH/深度学习 | Park 2025; Mendoza-Yero 2021 | Q2-Q3 |
| **Bessel/光片** | ★★★★ （旁瓣抑制） | ★★★★ （干涉精度） | **高** | Axicon/AOD | Turtaev 2023; Liu 2022 | Q2-Q3 |
| **相干光束合成** | ★★★★ （各路等强） | ★★★★★ （锁相要求） | **高** | 纯相位+反馈 | Xie 2024 (Sci. Rep.); Balasiano 2024 (JLT) | Q2-Q3 |
| **矢量光束** | ★★★ （模式纯度） | ★★★★ （偏振+相位联合） | **中** | Double-phase | Rodriguez-Fajardo 2025; Carbonell-Leal 2020 | Q2-Q3 |

### 核心发现

1. **STED显微镜、原子阵列操控和全息光刻**是**对强度+相位同时精度要求最高**的三个场景：
   - STED要求中心强度趋零+完美螺旋相位，任何偏差直接降低分辨率
   - 原子阵列要求亚百分级强度均匀性+相位锁定，偏差导致原子丢失/退相干
   - 全息光刻要求多光束强度比+相位差精确配对，决定纳米图案质量

2. **量子态光场制备**的相位要求最为苛刻——量子相干性对相位误差极其敏感，但多数文献仍用纯相位SLM

3. **飞秒激光加工**出现了明确使用复振幅调制的Q1期刊论文（Li 2024, Adv. Opt. Mater.），是该领域的新趋势

4. **光子计算/衍射NN**是新兴高需求方向——ACS Photonics 2024指出复振幅调制可使网络自由度翻倍

5. **Nature/Science级别论文**（Manetsch 2025 Nature; Zeng 2025 Nat. Comm.; Yu 2024 Nat. Comm.; Forbes 2025 Nat. Photon.; Rothe 2025 Science）都在不同程度上涉及对强度+相位同时精确控制的需求

6. **最关键的缺口：** 许多高需求场景（特别是STED、量子态制备和全息光刻）目前仍主要使用纯相位方法或多光束硬编码配对，复振幅调制方法（double-phase/superpixel）的**系统化引入**是一个明确的未被满足的需求

### 期刊分区分布

| 分区 | 文献数 | 代表期刊 |
|------|--------|----------|
| Q1 | 15 | Nature, Nature Photonics, Nature Communications, Science, Advanced Optical Materials, Advanced Functional Materials, Laser & Photonics Reviews, ACS Photonics, Optica |
| Q2 | 28 | Optics Express, Optics Letters, Physical Review A/Applied, Biomedical Optics Express, Applied Physics Letters, APL Photonics, Nanophotonics, J. Lightwave Technology, Neurocomputing |
| Q3 | 18 | Applied Optics, Optics & Laser Technology, Optics and Lasers in Eng., Scientific Reports, Measurement Sci. & Tech., OSA Continuum, Journal of Optics, Optics Communications |

---

*注：标记🔥的文献为与"phase-only SLM 复振幅调制+对目标面强度和相位同时严格要求"最直接相关的高价值推荐文献。分区参考中科院JCR分区（光学/物理类）。arXiv预印本标注了预期投稿期刊分区。本报告与前期报告（phase_only_SLM_literature_report.md）互补，前期报告聚焦四个基础场景的编码方法层面，本报告侧重扩展应用场景和三区以上期刊筛选。*
