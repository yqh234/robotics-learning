# 每日机器人论文对比
我认为今天最值得补的不是再加一篇泛化的大模型论文，而是把机器人抓取链路里更底层的两段补齐：目标位姿怎么估准，杂乱场景里的抓取候选怎么生成。
更新时间：2026-06-19 追加刷新

论文库地址：./papers/index.html

> 今日主题：用 DenseFusion 和 Contact-GraspNet 这组“6D 位姿估计 + 6-DoF 抓取生成”组合，补足当前论文库里抓取 / 深度感知 / 操作执行接口这一段。

## 论文 1

**DenseFusion: 6D Object Pose Estimation by Iterative Dense Fusion（2026-06-19）**

论文链接：https://arxiv.org/abs/1901.04780

为什么推荐：经典 RGB-D 6D 位姿估计代表作，CVPR 2019，Semantic Scholar 约 1146 引用，YCB-Video / LineMOD 体系长期复用。

## 论文 2

**Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes（2026-06-19）**

论文链接：https://arxiv.org/abs/2103.14127

为什么推荐：高代表性的杂乱场景 6-DoF 抓取生成工作，ICRA 2021，Semantic Scholar 约 470 引用，NVLabs 开源代码长期被后续工作引用。

## 对比结论

DenseFusion 负责“看准物体姿态”。
Contact-GraspNet 负责“从深度里提出可抓候选”。
两篇连起来，更接近真实机器人抓取系统的前半段。