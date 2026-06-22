# ZYNQ7020 图像处理 FPGA 课程设计

本仓库整理了 `zynq7020-image-processing` 相关基础实验与拓展实验工程，包含 Verilog/SDK 源码、上板现象图片、资源与时序截图以及 Markdown 实验报告。老师可直接点击下方链接在 GitHub 网页中查看报告。

## 报告入口

| 实验 | 内容 | 报告 |
| --- | --- | --- |
| 实验 0 | RTL 仿真与 Sobel 数据流验证 | [sobel_00_rtl_仿真报告.md](sobel_00_rtl_sim/sobel_00_rtl_仿真报告.md) |
| 实验 1 | HDMI 图像显示与红色边框拓展 | [sobel_01_hdmi_pattern_实验报告.md](sobel_01_hdmi_pattern_expand/sobel_01_hdmi_pattern_实验报告.md) |
| 实验 2 | HDMI Sobel 边缘检测与反色显示拓展 | [sobel_02_hdmi_sobel_实验报告.md](sobel_02_hdmi_sobel_expand/sobel_02_hdmi_sobel_实验报告.md) |
| 实验 3 | UART 输入图像 HDMI 显示与边框拓展 | [sobel_03_uart_hdmi_实验报告.md](sobel_03_uart_hdmi_expand/sobel_03_uart_hdmi_实验报告.md) |
| 实验 4 | UART 输入图像 Sobel 边缘检测与反色拓展 | [sobel_04_uart_sobel_hdmi_实验报告.md](sobel_04_uart_sobel_hdmi_expand/sobel_04_uart_sobel_hdmi_实验报告.md) |

## 目录说明

```text
sobel_00_rtl_sim/
    RTL 仿真工程、输入输出图像、波形截图与仿真报告

sobel_01_hdmi_pattern_expand/
    实验一拓展工程、上板图片、资源/时序截图与实验报告

sobel_02_hdmi_sobel_expand/
    实验二拓展工程、Sobel 输出图片、资源/时序截图与实验报告

sobel_03_uart_hdmi_expand/
    实验三拓展工程、串口输入显示图片、资源/时序截图与实验报告

sobel_04_uart_sobel_hdmi_expand/
    实验四拓展工程、UART + Sobel + HDMI 上板图片、资源/时序截图与实验报告
```

## 提交说明

仓库中保留了实验源码、工程配置、报告和必要图片。Vivado/SDK 的可再生成缓存、仿真大波形文件和运行中间产物未纳入版本控制，以避免仓库体积过大。
