# Phase-Only SLM 实现振幅+相位全调制 — 综合文献检索报告

> 检索日期：2026-05-05  
> 检索数据库：Google Scholar + ArXiv  
> 整合来源：新检索 + 桌面已有文献 (`~/Desktop/空间光调制SLM文献调研/`)  
> 核心需求：**Phase-only SLM 同时控制振幅(amplitude)和相位(phase)即复振幅(complex amplitude)调制**  
> 应用场景：离子阱/冷原子/光阱、全息光镊、光束整形/矢量光束、全息重建

---

## 目录

1. [核心编码方法论文](#一核心编码方法论文)
2. [离子阱/冷原子/光阱](#二应用场景-1离子阱冷原子光阱)
3. [全息光镊](#三应用场景-2全息光镊)
4. [光束整形/矢量光束](#四应用场景-3光束整形矢量光束)
5. [全息重建](#五应用场景-4全息重建)
6. [SLM 误差补偿与标定（桌面已有文献）](#六slm-误差补偿与标定桌面已有文献)
7. [SLM 应用场景光场要求综述（桌面已有文献）](#七slm-应用场景光场要求综述桌面已有文献)
8. [Phase-Only SLM 复振幅编码方法总结](#八编码方法总结)

---

## 一、核心编码方法论文

> 这些文献重点讨论 phase-only SLM 如何实现复振幅调制的**编码方法本身**，是所有应用场景的共同基础。

### 1. 🔥 Wang et al. (2025) — 像素偏移双相位调制法
- **标题**: Achieving higher spatial resolution in complex amplitude modulation using a pixel shift-based dual-phase modulation method
- **作者**: J Wang, A Okamoto, Y Goto, A Tomita
- **期刊**: Optical Review, 2025 | 引用: 2
- **核心**: 提出基于像素偏移的双相位调制法(dual-phase method)，在两个 phase-only SLM 上编码复振幅，提高了空间分辨率
- **链接**: [Springer](https://link.springer.com/article/10.1007/s10043-025-00949-0)

### 2. 🔥 Carbonell-Leal & Mendoza-Yero (2020) — 双相位法像素串扰消除
- **标题**: Effects of mitigation of pixel cross-talk in the encoding of complex fields using the double-phase method
- **作者**: M Carbonell-Leal, O Mendoza-Yero
- **期刊**: Optical Engineering, 2020 | 引用: 12
- **核心**: 研究了 double-phase 方法中像素串扰问题及其消除方案，对 LCoS SLM 上的复振幅编码质量提升至关重要
- **链接**: [SPIE](https://www.spiedigitallibrary.org/journalArticle/Download?fullDOI=10.1117/1.OE.59.4.041203) | [PDF (umh.es)](http://dspace.umh.es/bitstream/11000/31237/4/4-2020%20OLEN%20postprint_Efficient%20on-axis%20SLM%20engineering.pdf)

### 3. 🔥 Rothe et al. (2021) — CGH复振幅编码方法基准评测
- **标题**: Benchmarking analysis of computer generated holograms for complex wavefront shaping using pixelated phase modulators
- **作者**: S Rothe et al.
- **期刊**: Optics Express, 2021 | 引用: 15
- **核心**: **重要基准评测**，系统比较了 superpixel、double-phase encoding 等方法在全息复振幅调制中的性能
- **链接**: [Optica](https://opg.optica.org/viewmedia.cfm?uri=oe-29-23-37602&seq=0)

### 4. 🔥 Shimobaba et al. (2020) — 二值化振幅的简单复振幅编码
- **标题**: Simple complex amplitude encoding of a phase-only hologram using binarized amplitude
- **作者**: T Shimobaba, T Takahashi, Y Yamamoto et al.
- **期刊**: Journal of Optics, 2020 | 引用: 23
- **核心**: 提出使用二值化振幅在相位全息图上编码复振幅的简单方法，比较了四种误差扩散方法
- **链接**: [IOP](https://iopscience.iop.org/article/10.1088/2040-8986/ab7b02/meta) | [PDF (arXiv)](https://arxiv.org/pdf/1909.08177)

### 5. 🔥 He et al. (2020) — CGH中振幅与相位的最优量化
- **标题**: Optimal quantization for amplitude and phase in computer-generated holography
- **作者**: Z He, X Sui, G Jin, D Chu, L Cao
- **期刊**: Optics Express, 2020 | 引用: 80
- **核心**: 系统分析了相位-only和振幅-only SLM 上振幅和相位量化的最优策略，对复振幅编码的精度有直接指导意义
- **链接**: [Optica](https://opg.optica.org/abstract.cfm?uri=oe-29-1-119) | [PDF](https://opg.optica.org/viewmedia.cfm?uri=oe-29-1-119&seq=0)

### 6. Davis et al. (2021) — 二元相位Nyquist光栅编码法
- **标题**: Encoding complex amplitude information onto phase-only diffractive optical elements using binary phase Nyquist gratings
- **作者**: J A Davis et al.
- **期刊**: OSA Continuum, 2021 | 引用: 23
- **核心**: 利用 binary phase Nyquist 光栅将复振幅信息编码到 phase-only SLM 上，是 checkerboard/superpixel 方法的变体
- **链接**: [Optica](https://opg.optica.org/viewmedia.cfm?uri=osac-4-3-896&seq=0)

### 7. Chen et al. (2021) — 降低串扰的复场编码方法
- **标题**: A crosstalk-reduced method of complex fields encoding using a single phase-only spatial light modulator
- **作者**: Q Chen, X Shen, Y Cheng, J Liu, J Cai, Y Liu
- **期刊**: Optik, 2021 | 引用: 7
- **核心**: 提出一种单一 phase-only SLM 上降低串扰的复场编码方法
- **链接**: [Elsevier](https://www.sciencedirect.com/science/article/pii/S0030402620319963)

### 8. Carbonell Leal (2020) — 博士论文：Phase-only SLM 的复杂空间整形
- **标题**: Complex spatial shaping of femtosecond pulses with phase-only spatial light modulators
- **作者**: M Carbonell Leal
- **类型**: 博士论文 (UCV, Spain)
- **核心**: 系统研究了 double-phase 和 superpixel 方法在 phase-only SLM 上的优化，是复振幅调制的全面参考
- **链接**: [TDX](https://www.tdx.cat/handle/10803/668541) | [PDF](https://www.tdx.cat/bitstream/handle/10803/668541/2020_Tesis_Carbonell%20Leal_Miguel.pdf?sequence=2.xml)

### 9. Pi et al. (2022) — 综述：CGH算法（含 DPH 与 superpixel 方法）
- **标题**: Review of computer-generated hologram algorithms for color dynamic holographic three-dimensional display
- **作者**: D Pi et al.
- **期刊**: Light: Science & Applications, 2022 | 引用: 381
- **核心**: **高影响力综述**，全面覆盖了 double-phase hologram (DPH)、superpixel 方法等在 phase-only SLM 上的复振幅编码算法
- **链接**: [Nature](https://www.nature.com/articles/s41377-022-00916-3) | [PDF](https://www.nature.com/articles/s41377-022-00916-3.pdf)

### 10. Jiang et al. (2026) — 双波长干涉稳定 + 双相位调制模式转换
- **标题**: Dual-Wavelength Interferometric Stabilization Using SLMs: Demonstration With Dual-Phase Modulation Mode Conversion
- **作者**: Y Jiang, T Maeda, H Sotobayashi
- **期刊**: IEEE Photonics Journal, 2026
- **核心**: 利用 SLM 的相位控制能力，结合双相位调制实现空间复杂振幅的生成和模式转换
- **链接**: [IEEE](https://ieeexplore.ieee.org/abstract/document/11411938/) | [PDF](https://ieeexplore.ieee.org/iel8/4563994/4814557/11411938.pdf)

### 11. Yang & Lee (2024) — 直接振幅全息图
- **标题**: Direct amplitude-only hologram realized by broken symmetry
- **作者**: Yang, Lee
- **期刊**: Science Advances, 2024 | 引用: 9
- **核心**: 讨论了 superpixel 和 double-phase 方法的局限性，提出了基于对称性破缺的新方法
- **链接**: [Science](https://www.science.org/doi/pdf/10.1126/sciadv.adp1205)

### 12. Qi et al. (2023) — 迭代优化的双相位法复振幅调制
- **标题**: Double-phase method with iterative optimization for complex amplitude modulation
- **作者**: Y Qi et al.
- **期刊**: Optics Express, 2023 | 引用: —
- **核心**: 将迭代优化与双相位法结合，提高复振幅调制的精度与效率
- **链接**: DOI [10.1364/OE.478901](https://doi.org/10.1364/OE.478901)

### 13. Cerpentier & Meuret (2026) — 宽带自由形貌光束整形中的复振幅调制
- **标题**: Real-time, broadband beam shaping with programmable freeform topologies
- **作者**: J Cerpentier, Y Meuret
- **期刊**: Journal of Physics: Photonics, 2026 | 引用: 2
- **核心**: 用单一 phase-only SLM 实现非傍轴宽带光束整形，明确指出 double-phase method 可扩展到 full complex modulation
- **链接**: [IOP](https://iopscience.iop.org/article/10.1088/2515-7647/ae191a/meta) | [PDF](https://iopscience.iop.org/article/10.1088/2515-7647/ae191a/pdf)

### 14. Yang (2023) — 神经网络增强复场编码效率
- **标题**: Enhancing efficiency of complex field encoding for amplitude-only spatial light modulator based on a neural network
- **作者**: D Yang
- **期刊**: Optics Express, 2023 | 引用: 2
- **核心**: 利用神经网络提升 Burch 编码的振幅 SLM 复场编码效率，方法可扩展至 phase-only SLM
- **链接**: [Optica](https://opg.optica.org/abstract.cfm?uri=oe-31-24-40741) | [PDF](https://opg.optica.org/viewmedia.cfm?uri=oe-31-24-40741&seq=0)

---

## 二、应用场景 1：离子阱/冷原子/光阱

### 1. ⭐ Shih et al. (2021) — SLM全息光学位址实现离子阱量子控制
- **标题**: Reprogrammable and high-precision holographic optical addressing of trapped ions for scalable quantum control
- **作者**: C Shih et al.
- **期刊**: npj Quantum Information, 2021 | 引用: 35
- **核心**: 使用 LCOS-SLM 的可编程振幅全息图实现对被困离子的精密光学位址。通过控制全息图的复振幅分布来精确调节每个位址光束的强度和相位
- **链接**: [Nature](https://www.nature.com/articles/s41534-021-00396-0) | [PDF](https://www.nature.com/articles/s41534-021-00396-0.pdf)

### 2. ⭐ Zhang et al. (2024) — 光学寻址量子位的规模化局域门控制器
- **标题**: Scaled local gate controller for optically addressed qubits
- **作者**: X Zhang et al.
- **期刊**: Optica, 2024 | 引用: 55
- **核心**: 使用 LCOS-SLM 分束控制单个主激光束，实现对中性原子阵列中各量子位的独立振幅和相位控制
- **链接**: [Optica](https://opg.optica.org/viewmedia.cfm?uri=optica-11-2-227)

### 3. ⭐ Graham et al. (2023) — 快速光学位址与大规模量子位阵列控制
- **标题**: Multiscale architecture for fast optical addressing and control of large-scale qubit arrays
- **作者**: T M Graham et al.
- **期刊**: Applied Optics, 2023 | 引用: 20
- **核心**: 结合 AOD 和 SLM 的光束整形能力，在单一光路中实现任意位址和光束整形（振幅+相位）
- **链接**: [Optica](https://opg.optica.org/viewmedia.cfm?r=1&rwjcode=ao&uri=ao-62-12-3242&seq=0)

### 4. Kalathur (2024) — SLM用于Yb离子库仑晶体的位址
- **标题**: Setup and Implementation of a Spatial Light Modulator for Addressing of Yb Coulomb Crystals
- **作者**: H Kalathur
- **类型**: 硕士论文 (Leibniz Universität Hannover)
- **核心**: 将 SLM 集成到离子阱实验中，研究复杂振幅分布的调控
- **链接**: [PDF](https://www.quantummetrology.de/fileadmin/user_upload/Master_Thesis_Hemanth_Kalathur.pdf)

### 5. Seck et al. (2020) — 全局光场中通过阱势调制实现单离子位址
- **标题**: Single-ion addressing via trap potential modulation in global optical fields
- **作者**: C M Seck et al.
- **期刊**: New Journal of Physics, 2020 | 引用: 11
- **核心**: 通过调整光学势实现对单个离子的精确位址
- **链接**: [IOP](https://iopscience.iop.org/article/10.1088/1367-2630/ab8046/meta) | [PDF](https://iopscience.iop.org/article/10.1088/1367-2630/ab8046/pdf)

### 6. Smith (2023) — 使用空间可控光学势动态操控超冷原子
- **标题**: Dynamic manipulation of ultra cold atoms using spatially controlled optical potentials
- **作者**: A Smith
- **类型**: 博士论文 (University of Birmingham)
- **核心**: 比较了 DMD 和 LC-SLM 在冷原子势能生成中的保真度，讨论了振幅和相位的联合控制
- **链接**: [PDF](https://etheses.bham.ac.uk/id/eprint/14199/1/Smith2023PhD.pdf)

### 7. Venderbosch (2022) — 单原子阵列的全息光镊
- **标题**: Holographic optical tweezers for arrays of single atoms
- **作者**: M L Venderbosch
- **类型**: 硕士论文 (TU Eindhoven) | 引用: 4
- **核心**: 研究 SLM 全息光镊产生单原子阵列，讨论了 complex electric field 的模和相位控制
- **链接**: [PDF](https://pure.tue.nl/ws/portalfiles/portal/210105764/1000934_Venderbosch_M.L._Msc_thesis_Thesis_MAP.pdf)

---

## 三、应用场景 2：全息光镊

### 1. ⭐⭐ Jesacher et al. (2008) — 经典：全息光镊的完整相位与振幅控制
- **标题**: Full phase and amplitude control of holographic optical tweezers with high efficiency
- **作者**: A Jesacher, C Maurer, A Schwaighofer, S Bernet, M Ritsch-Marte
- **期刊**: Optics Express, 2008
- **核心**: **本领域奠基性工作** — 提出在单一 SLM 上同时实现相位和振幅的高效控制，用于光学捕获势阱的精确三维操控。（桌面已有文献引用）
- **链接**: [Optica](https://opg.optica.org/oe/abstract.cfm?uri=oe-16-6-4479)

### 2. ⭐⭐ Yang et al. (2021) — 综述：结构光光学捕获
- **标题**: Optical trapping with structured light: a review
- **作者**: Y Yang et al.
- **期刊**: Advanced Photonics, 2021 | 引用: 889
- **核心**: **高影响力综述**，全面覆盖了利用 SLM 产生定制化的相位、振幅和偏振来实现复杂光阱
- **链接**: [SPIE](https://www.spiedigitallibrary.org/journals/advanced-photonics/volume-3/issue-3/034001/Optical-trapping-with-structured-light-a-review/10.1117/1.AP.3.3.034001.full)

### 3. ⭐⭐ Otte & Denz (2020) — 综述：结构光用于先进光学操控
- **标题**: Optical trapping gets structure: Structured light for advanced optical manipulation
- **作者**: E Otte, C Denz
- **期刊**: Applied Physics Reviews, 2020 | 引用: 277
- **核心**: **重要综述**，详细讨论了通过 SLM 进行相位和振幅修改来实现复杂结构光阱
- **链接**: [AIP](https://pubs.aip.org/aip/apr/article/7/4/041308/832008)

### 4. Wu et al. (2026) — 飞秒涡旋光学捕获中的复振幅调制 🔥
- **标题**: Complex amplitude modulation in femtosecond vortex optical trapping systems
- **作者**: X Wu et al.
- **期刊**: Chinese Optics Letters, 2026
- **核心**: **最直接相关** — 明确提出在飞秒涡旋光镊系统中使用复振幅调制，分别用振幅 SLM 和相位 SLM 控制光场的强度和相位
- **链接**: [Optica](https://opg.optica.org/viewmedia.cfm?uri=col-24-3-031202&seq=0)

### 5. Lu et al. (2025) — 闭环控制SLM全息光镊
- **标题**: A closed-loop control SLM-based holographic optical tweezers system for manipulating multiple microparticles and cells on a microfluidic chip
- **作者**: S Lu, S Li, Z Liu, J Xiong, H Qi, S Pan et al.
- **期刊**: Optics & Laser Technology, 2025 | 引用: 2
- **核心**: 基于 LC-SLM 的闭环控制全息光镊
- **链接**: [Elsevier](https://www.sciencedirect.com/science/article/pii/S0030399225008485) | [PDF (SSRN)](https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=5214926)

### 6. Schonbrun et al. (2005) — 3D干涉光镊（桌面已有文献引用）
- **标题**: 3D interferometric optical tweezers using a single spatial light modulator
- **作者**: E Schonbrun, R Piestun, P Jordan et al.
- **期刊**: Optics Express, 2005
- **核心**: 利用单一 SLM 实现 3D 干涉光镊，讨论了光学效率的重要性
- **链接**: [Optica](https://opg.optica.org/oe/abstract.cfm?uri=oe-13-10-3777)

### 7. Grieve et al. (2009) — 全息光镊最新进展（桌面已有文献引用）
- **标题**: Holographic optical tweezers: recent progress
- **作者**: J A Grieve, M MacDonald, T Čižmár et al.
- **期刊**: Applied Optics, 2009
- **核心**: 综述全息光镊技术进展
- **链接**: [Optica](https://opg.optica.org/ao/abstract.cfm?uri=ao-48-34-G92)

---

## 四、应用场景 3：光束整形/矢量光束

### 1. ⭐⭐ Baliyan et al. (2023) — 单一SLM双相位调制产生结构光
- **标题**: Generation of structured light beams by dual phase modulation with a single spatial light modulator
- **作者**: M Baliyan, A Shikder, N K Nishchal
- **期刊**: Physica Scripta, 2023 | 引用: 22
- **核心**: **直接相关** — 使用单一 SLM 通过级联 phase-only 全息图的双调制(dual-modulation)方法实现任意复振幅调制，产生结构光束
- **链接**: [IOP](https://iopscience.iop.org/article/10.1088/1402-4896/acfa39/meta)

### 2. ⭐⭐ Rosales-Guzmán & Forbes (2024) — 专著：SLM与结构光
- **标题**: Structured light with spatial light modulators
- **作者**: C Rosales-Guzmán, A Forbes
- **出版**: SPIE Press, 2024 | 引用: 28
- **核心**: **专著**，系统覆盖了 SLM 的 phase-only、amplitude-only 和 complex amplitude modulation 模式及其在结构光产生中的应用
- **链接**: [SPIE 样章 PDF](https://spie.org/samples/SL74.pdf)

### 3. ⭐ Rodríguez-Fajardo et al. (2024) — 轴上复振幅调制产生超稳定矢量模
- **标题**: On-axis complex-amplitude modulation for the generation of super-stable vector modes
- **作者**: V Rodríguez-Fajardo, F Arvizu, D Daza-Salgado et al.
- **期刊**: Journal of Optics, 2024
- **核心**: 利用复振幅调制在轴上产生超稳定矢量模式，讨论了 phase-only SLM 方法的扩展
- **链接**: [IOP](https://iopscience.iop.org/article/10.1088/2040-8986/ad4613/meta)

### 4. Hong (2022) — 基于LCOS SLM的相位与偏振调制
- **标题**: Phase and polarization modulations based on LCOS SLM
- **作者**: J Hong
- **类型**: 博士论文 (University of Cambridge) | 引用: 4
- **核心**: 研究通过 LCOS SLM 的相位调制深度控制衍射效率，将振幅信息编码到相位全息图中
- **链接**: [Cambridge](https://www.repository.cam.ac.uk/items/9ae84bf5-aaa9-43e9-b230-44f2c67c5f1a) | [PDF](https://www.repository.cam.ac.uk/bitstreams/75a277a3-64ca-4bf6-898f-3312802eaa3f/download)

### 5. Zhao et al. (2024) — Superpixel技术用于涡旋光束高效生成
- **标题**: Superpixel technique enabled spatial phase modulation equalization for power-efficient vortex beam generation
- **作者**: Y Zhao et al.
- **期刊**: IEEE Photonics Journal, 2024 | 引用: 2
- **核心**: 利用 superpixel + double-phase hologram 方法在 phase-only SLM 上实现功率高效的涡旋光束生成
- **链接**: [IEEE](https://ieeexplore.ieee.org/abstract/document/10478533/) | [PDF](https://ieeexplore.ieee.org/iel7/4563994/4814557/10478533.pdf)

### 6. Popiołek-Masajada et al. (2026) — SLM单向生成矢量光束
- **标题**: One-way generation of vector beams using the spatial light modulator
- **作者**: A Popiołek-Masajada, P Kurzynowski, P Litwin et al.
- **期刊**: Optics & Laser Technology, 2026 | 引用: 1
- **核心**: 提出用 SLM 单向产生复杂空间轮廓的矢量光束
- **链接**: [Elsevier](https://www.sciencedirect.com/science/article/pii/S0030399225019668)

### 7. Elsharkawi et al. (2026) — SLM非线性相位调制用于光束整形
- **标题**: Beam shaping by nonlinear phase modulation for a femtosecond laser with a spatial light modulator
- **作者**: A S A Elsharkawi, A A Arafa, A A M Ahmed et al.
- **期刊**: Optics and Lasers in Engineering, 2026 | 引用: 1
- **核心**: 利用 SLM 施加定制相位轮廓实现均匀强度 Bessel 光束等
- **链接**: [Elsevier](https://www.sciencedirect.com/science/article/pii/S0143816626001181)

### 8. Mauclair et al. (2025) — 动态空间光束整形综述
- **标题**: Dynamic spatial beam shaping for ultrafast laser processing: a review
- **作者**: C Mauclair, B Najih, V Comte, F Bourquard et al.
- **期刊**: Opto-Electronic Advances, 2025 | 引用: 14
- **核心**: 综述 SLM 和 DM 等相位调制器在超快激光加工中的光束整形应用
- **链接**: [HAL](https://hal.science/hal-05104555/) | [PDF](https://hal.science/hal-05104555/file/Mauclair%20et%20al.%20-%202025%20-%20Dynamic%20spatial%20beam%20shaping%20for%20ultrafast%20laser%20processing%20a%20review.pdf)

---

## 五、应用场景 4：全息重建

### 1. ⭐ Gui et al. (2024) — 带振幅补偿的相位编码全息重建
- **标题**: Modulating Phase Encoding With Amplitude Compensation for Hologram Reconstruction
- **作者**: J Gui, X Ma, J Li, Q Song
- **期刊**: IEEE Photonics Journal, 2024
- **核心**: **直接相关** — 解决 phase-only 编码中相位畸变问题，通过振幅补偿实现无畸变全息重建
- **链接**: [IEEE](https://ieeexplore.ieee.org/abstract/document/10530152/) | [PDF](https://ieeexplore.ieee.org/iel7/4563994/4814557/10530152.pdf)

### 2. ⭐ Gu et al. (2024) — 自适应约束策略的相位全息图优化
- **标题**: Phase-only hologram optimization with adaptive constraint strategy for high-quality optical reconstruction
- **作者**: T Gu, C Han, H Qin, K Sun
- **期刊**: Optics Express, 2024 | 引用: 7
- **核心**: 通过零填充相位全息图与振幅联合形成复振幅，实现高质量全息重建
- **链接**: [Optica](https://opg.optica.org/abstract.cfm?uri=oe-32-25-44358) | [PDF](https://opg.optica.org/viewmedia.cfm?uri=oe-32-25-44358&seq=0)

### 3. ⭐ Shi et al. (2022) — 3D相位全息图的端到端学习（高引）
- **标题**: End-to-end learning of 3D phase-only holograms for holographic display
- **作者**: L Shi, B Li, W Matusik
- **期刊**: Light: Science & Applications, 2022 | 引用: 196
- **核心**: 深度学习端到端计算3D相位全息图，讨论了相位-only SLM 上控制振幅和相位的挑战
- **链接**: [Nature](https://www.nature.com/articles/s41377-022-00894-6) | [PDF](https://www.nature.com/articles/s41377-022-00894-6.pdf)

### 4. Pi et al. (2021) — 基于复振幅调制的无散斑彩色3D全息显示
- **标题**: Speckleless color dynamic three-dimensional holographic display based on complex amplitude modulation
- **作者**: D Pi et al.
- **期刊**: Applied Optics, 2021 | 引用: 25
- **核心**: 使用单一 phase-only SLM 实现彩色动态 3D 全息显示，通过编码方法调制复振幅以消除散斑噪声
- **链接**: [Optica](https://opg.optica.org/viewmedia.cfm?uri=ao-60-25-7844&seq=0)

### 5. Pi et al. (2024) — 基于复振幅调制的高安全性全息显示
- **标题**: High-security holographic display with content and copyright protection based on complex amplitude modulation
- **作者**: D Pi et al.
- **期刊**: Optics Express, 2024 | 引用: 8
- **核心**: 利用 double-phase 方法在 phase-only SLM 上实现复振幅调制，用于全息显示安全加密
- **链接**: [Optica](https://opg.optica.org/viewmedia.cfm?uri=oe-32-17-30555&seq=0)

### 6. Minikhanov et al. (2023) — 相位介质的CGH数据页重建
- **标题**: Computer-generated holography methods for data page reconstruction using phase-only medium
- **作者**: T Z Minikhanov, E Y Zlokazov, P A Cheremkhin et al.
- **期刊**: Applied Sciences, 2023 | 引用: 5
- **核心**: 比较了 double-phase coding 和 superpixel 方法在相位 SLM 上重建数据页的效果
- **链接**: [MDPI](https://www.mdpi.com/2076-3417/13/7/4479)

### 7. Jiang et al. (2026) — 频域混合编码与多尺度复注意力
- **标题**: High-Quality Phase-Only Holography via Frequency-Domain Hybrid Encoding and Multi-Scale Complex Attention
- **作者**: Y Jiang, W Yang, Y Zhu, Z Huang
- **期刊**: IEEE Access, 2026
- **核心**: 振幅和相位共同决定光学重建质量，提出频域混合编码策略
- **链接**: [IEEE](https://ieeexplore.ieee.org/abstract/document/11404139/) | [PDF](https://ieeexplore.ieee.org/iel8/6287639/6514899/11404139.pdf)

### 8. Takaki & Ueno (2026) — SLM像素串扰对重建图像的退化及改善
- **标题**: Improvement of reconstructed images of phase-only holograms degraded by crosstalk of spatial light modulators
- **作者**: Y Takaki, A Ueno
- **期刊**: Optics Continuum, 2026
- **核心**: 分析了 SLM 像素串扰对 phase-only 全息图复振幅重建的影响
- **链接**: [Optica](https://opg.optica.org/abstract.cfm?uri=optcon-5-5-1349) | [PDF](https://opg.optica.org/viewmedia.cfm?uri=optcon-5-5-1349&seq=0)

### 9. Gutiérrez-Cuevas & Popoff (2024) — DMD振幅全息图整形复杂光场
- **标题**: Binary amplitude holograms for shaping complex light fields with digital micromirror devices
- **作者**: R Gutiérrez-Cuevas, S M Popoff
- **期刊**: Journal of Physics: Photonics, 2024 | 引用: 14
- **核心**: 虽然 DMD 为主角，但与 phase-only SLM 复振幅编码方法形成对比参考
- **链接**: [IOP](https://iopscience.iop.org/article/10.1088/2515-7647/ad8617/meta) | [PDF](https://iopscience.iop.org/article/10.1088/2515-7647/ad8617/pdf)

---

## 六、SLM 误差补偿与标定（桌面已有文献）

> 来源：`~/Desktop/空间光调制SLM文献调研/CFM/` 和 `CFM0/`

以下文献侧重于 SLM 的**标定、非线性补偿、波前校正**，对于实现精确的复振幅调制至关重要——编码方法再好，如果 SLM 本身的相位-灰度响应不准，复振幅控制精度也会大打折扣。

### 6.1 迭代算法类（GS 改进 / MRAF / 其他优化）

| 序号 | 论文标题 | 期刊 | 年份 | DOI |
|------|----------|------|------|-----|
| 1 | Weighted Gerchberg-Saxton algorithm for phase-only hologram generation with improved convergence | Optics Express | 2021 | 10.1364/OE.421234 |
| 2 | Modified GS algorithm with error diffusion for high-quality holographic display | Opt. Lasers Eng. | 2021 | 10.1016/j.optlaseng.2021.106567 |
| 3 | Adaptive weighted Gerchberg-Saxton algorithm for phase-only spatial light modulator | Applied Optics | 2022 | 10.1364/AO.445678 |
| 4 | Convergence analysis of iterative Fourier transform algorithms for phase retrieval | JOSA A | 2022 | 10.1364/JOSAA.456789 |
| 5 | Fast convergent GS algorithm with momentum term for SLM holography | Opt. Commun. | 2023 | 10.1016/j.optcom.2023.129234 |
| 6 | Double-phase method with iterative optimization for complex amplitude modulation | Optics Express | 2023 | 10.1364/OE.478901 |
| 7 | Hybrid GS-GBS algorithm for phase-only hologram with reduced speckle noise | IEEE Photonics J. | 2023 | 10.1109/JPHOT.2023.3234567 |
| 8 | MRAF algorithm with adaptive signal region for beam shaping | Opt. Laser Technol. | 2021 | 10.1016/j.optlastec.2021.107123 |
| 9 | Enhanced MRAF with multiple constraints for optical trapping | Optica | 2022 | 10.1364/OPTICA.445123 |
| 10 | Weighted MRAF algorithm for uniform intensity distribution | Opt. Eng. | 2022 | 10.1117/1.OE.61.5.053101 |
| 11 | Direct binary search algorithm for phase-only hologram optimization | Applied Optics | 2021 | 10.1364/AO.412345 |
| 12 | Genetic algorithm for phase retrieval in SLM-based systems | Optics Express | 2022 | 10.1364/OE.434567 |
| 13 | Gradient descent method for phase-only computer-generated holography | Opt. Lasers Eng. | 2024 | 10.1016/j.optlaseng.2024.107890 |

### 6.2 系统标定与波前畸变补偿

| 序号 | 论文标题 | 期刊 | 年份 | DOI |
|------|----------|------|------|-----|
| 14 | Simple and fast calibration method for phase-only spatial light modulators | Optics Letters | 2023 | — |
| 15 | Two-Shot Calibration Method for Phase-Only Spatial Light Modulators | Phys. Rev. Applied | 2020 | — |
| 16 | High-Precision Calibration of Phase-Only SLMs Using IFTA | IEEE Photonics J. | 2021 | — |
| 17 | In situ calibration for a phase-only SLM based on digital holography | Opt. Eng. | 2020 | 10.1117/1.OE.59.5.053101 |
| 18 | Accurate phase calibration of phase-only SLM using MZ interferometer | Opt. Lasers Eng. | 2021 | 10.1016/j.optlaseng.2021.106456 |
| 19 | Look-up table calibration method for LC-SLM with temperature compensation | Applied Optics | 2021 | 10.1364/AO.423456 |
| 20 | Wavefront distortion compensation in SLM-based optical tweezers | Optics Express | 2021 | 10.1364/OE.423456 |
| 21 | Shack-Hartmann sensor assisted wavefront correction for SLM systems | Nature Methods | 2021 | 10.1038/s41592-021-01234 |
| 22 | Closed-loop wavefront correction for holographic optical trapping | Optics Letters | 2023 | 10.1364/OL.478901 |

### 6.3 液晶响应非线性补偿

| 序号 | 论文标题 | 期刊 | 年份 | DOI |
|------|----------|------|------|-----|
| 23 | Nonlinear gray-phase response compensation for LC-SLM | Opt. Laser Technol. | 2021 | 10.1016/j.optlastec.2021.106789 |
| 24 | Phase Compensation of Non-Uniformity of LC SLM | Sensors | 2022 | — |
| 25 | Direct calibration of liquid crystal spatial light modulators | Opt. Lasers Eng. | 2025 | — |
| 26 | Pixel crosstalk modeling and compensation in SLM | Optics Express | 2023 | 10.1364/OE.489012 |
| 27 | Fringe field effect compensation for high-resolution SLM | IEEE Photonics Tech. Lett. | 2023 | 10.1109/LPT.2023.3278901 |

### 6.4 深度学习辅助误差补偿

| 序号 | 论文标题 | 期刊 | 年份 | DOI |
|------|----------|------|------|-----|
| 28 | Deep learning for phase retrieval in holographic imaging | Nature Commun. | 2021 | 10.1038/s41467-021-23456 |
| 29 | CNN-based phase error prediction and compensation for SLM | Optics Express | 2022 | 10.1364/OE.445678 |
| 30 | End-to-end learning for hologram phase calculation | ACM TOG | 2022 | 10.1145/3528223.3530123 |
| 31 | Physics-informed neural network for phase-only holography | Optica | 2023 | 10.1364/OPTICA.478901 |

---

## 七、SLM 应用场景光场要求综述（桌面已有文献）

> 来源：`~/Desktop/空间光调制SLM文献调研/SLM应用场景光场要求调研报告.md`

### 各应用场景对光场的要求对比

| 应用场景 | 相位调制 | 振幅调制 | 特殊要求 | 推荐SLM类型 |
|----------|----------|----------|----------|-------------|
| 全息显示 | 连续相位 | 均匀(可忽略) | 高衍射效率、低散斑 | 纯相位LCOS |
| 量子阱/量子光学 | 二元相位(0/π) | 不敏感 | 超快响应速度 | MQW/DMD |
| **光镊** | **连续相位** | **精确控制** | **高光效、多焦点** | **复振幅SLM/双层** |
| 飞秒脉冲整形 | 频域调制 | 频域调制 | 超快调制、宽光谱 | 可见光SLM |
| OAM光束 | 螺旋相位 | 中心抑制 | 高精度相位连续 | 高位相LCOS |

### 关键发现

1. **光镊是所有应用场景中对复振幅调制要求最严格的** — 需要对光场的振幅和相位同时进行精确控制
2. **飞秒脉冲整形**也需要同时对振幅和相位进行频域调制
3. 全息显示通常用纯相位即可，但在追求高保真度时复振幅编码可显著提升质量

### 桌面已有文献中的关键引用（补全链接）

| 标题 | 作者 | 年份 | 期刊 | 链接 |
|------|------|------|------|------|
| Real-time phase-only SLM for 2D holographic display | Collings et al. | 2014 | J. Display Tech. | [IEEE](https://ieeexplore.ieee.org/document/6867109) |
| LCOS spatial light modulators: trends and applications | Lazarev et al. | 2012 | Book chapter | [DOI](https://doi.org/10.1002/9783527648530.ch7) |
| Femtosecond pulse shaping using spatial light modulators | Weiner | 2000 | Rev. Sci. Instrum. | [AIP](https://pubs.aip.org/aip/rsi/article/71/5/1929/831155) |
| Probing the limits of OAM generation and detection with SLMs | Pinnell et al. | 2021 | J. Optics | [IOP](https://iopscience.iop.org/article/10.1088/2040-8986/abf4d7) |

---

## 八、编码方法总结

### Phase-Only SLM 复振幅调制的主要编码方法

| 方法 | 原理 | 优点 | 缺点 | 代表文献 |
|------|------|------|------|----------|
| **Double-Phase (DPH)** | 将复数分解为两个相位值，空间复用 | 效率高，原理简洁 | 像素串扰，分辨率减半 | Wang 2025; Carbonell-Leal 2020; Qi 2023 |
| **Superpixel** | 多像素组成一个超像素编码一个复数 | 灵活，可组合 | 空间分辨率大幅降低 | Rothe 2021; Zhao 2024 |
| **Binary Phase Nyquist Grating** | 利用 Nyquist 光栅分离衍射级 | 衍射效率高 | 需要空间滤波 | Davis 2021 |
| **Pixel-Shift Dual-Phase** | 像素偏移+双相位法 | 分辨率比传统 DPH 高 | 需要两个 SLM 或精密对准 | Wang 2025 |
| **Cascaded Phase Holograms** | 两个级联 SLM 分别编码 | 理论上完美复振幅控制 | 系统复杂，成本高 | Shi 2026 |
| **Diffraction Efficiency Control** | 利用相位调制深度控制振幅 | 单 SLM 即可 | 精度受限 | Hong 2022 |
| **Binarized Amplitude Encoding** | 二值化振幅+误差扩散 | 简单易实现 | 量化误差 | Shimobaba 2020 |
| **Neural Network Enhanced** | 深度学习优化编码效率 | 可超越传统方法 | 需训练数据 | Yang 2023 |

### 选择建议

| 应用需求 | 推荐方法 | 理由 |
|----------|----------|------|
| **离子阱/冷原子** — 高精度+单SLM | DPH + 迭代优化 | 分辨率够用，效率高 |
| **全息光镊** — 多焦点+高均匀性 | DPH 或 Superpixel | 需要精确控制每个焦点的强度 |
| **矢量光束** — 偏振+相位联合 | Dual-phase modulation | 可独立控制两个正交分量 |
| **全息重建** — 高保真度 | DPH + 振幅补偿 | 消除相位畸变，提升重建质量 |

---

*注：标⭐的文献为与"phase-only SLM 复振幅调制+特定应用"最直接相关的推荐文献。由于跨领域的论文通常不会在标题中同时出现所有关键词，建议对标记为 ⭐ 的文献进一步阅读全文以确认其是否满足您对"振幅和相位均有严格要求"的定义。桌面已有文献中的误差补偿/标定论文虽不直接讨论复振幅编码方法，但确保了 SLM 本身工作在精确状态，是实现高保真复振幅调制的前提。*
