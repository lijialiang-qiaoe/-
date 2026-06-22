// Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2017.4 (win64) Build 2086221 Fri Dec 15 20:55:39 MST 2017
// Date        : Sun Jun 14 22:20:58 2026
// Host        : DESKTOP-210HI13 running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode synth_stub
//               F:/FPGA-course-main/FPGA-course-main/zynq7020-image-processing/sobel_01_hdmi_pattern/sobel_01_hdmi_pattern.srcs/sources_1/ip/video_clock/video_clock_stub.v
// Design      : video_clock
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7z020clg400-2
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
module video_clock(clk_out1, clk_out2, reset, locked, clk_in1)
/* synthesis syn_black_box black_box_pad_pin="clk_out1,clk_out2,reset,locked,clk_in1" */;
  output clk_out1;
  output clk_out2;
  input reset;
  output locked;
  input clk_in1;
endmodule
