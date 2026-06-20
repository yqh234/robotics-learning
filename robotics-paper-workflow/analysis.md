# 每日机器人论文对比
我认为今天最值得补的不是再加一篇泛化的大模型论文，而是把机器人抓取链路里更底层的两段补齐：目标位姿怎么估准，杂乱场景里的抓取候选怎么生成。
更新时间：2026-06-20 追加刷新

论文库地址：./papers/index.html

> 今日主题：用 FoundationPose 和 Dex-Net 2.0 这组“新物体 6D 位姿估计 + 经典抓取规划”组合，补足当前论文库里新感知能力 / 抓取底座 / 操作执行接口这一段。

## 论文 1

**FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects（2026-06-20）**

论文链接：https://arxiv.org/abs/2312.08344

为什么推荐：新物体 6D 位姿估计代表作，CVPR 2024，Semantic Scholar 约 563 引用，NVLabs 开源和后续部署分支都很活跃。

## 论文 2

**Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics（2026-06-20）**

论文链接：https://arxiv.org/abs/1703.09312

为什么推荐：经典抓取规划入口论文，RSS 2017，Semantic Scholar 约 1394 引用，用合成数据和解析抓取度量奠定了后续学习式抓取规划路线。

## 对比结论

FoundationPose 负责“把新物体姿态估准并跟稳”。
Dex-Net 2.0 负责“从深度里快速筛出高质量抓取候选”。
两篇连起来，更接近真实机器人抓取系统的前半段。