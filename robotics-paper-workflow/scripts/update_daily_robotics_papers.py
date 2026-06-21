from __future__ import annotations

import html
import os
import re
import shutil
import urllib.request
from pathlib import Path


ROOT = Path(r"C:\Users\86136\Documents\Codex\2026-06-15\codex-codex")
REPO_ROOT = ROOT / "work" / "robotics-learning"
WORKFLOW_ROOT = REPO_ROOT / "robotics-paper-workflow"
OUTPUTS_ROOT = ROOT / "outputs"
DESKTOP_ROOT = Path(r"C:\Users\86136\Desktop\机器人论文 PDFs")
TODAY = "2026-06-21"


PAPERS = [
    {
        "title": "Normalized Object Coordinate Space for Category-Level 6D Object Pose and Size Estimation",
        "slug": "nocs",
        "pdf_url": "https://openaccess.thecvf.com/content_CVPR_2019/papers/Wang_Normalized_Object_Coordinate_Space_for_Category-Level_6D_Object_Pose_and_CVPR_2019_paper.pdf",
        "arxiv_url": "https://arxiv.org/abs/1901.02970",
        "landing_url": "https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Normalized_Object_Coordinate_Space_for_Category-Level_6D_Object_Pose_and_CVPR_2019_paper.html",
        "doi_url": "https://doi.org/10.1109/CVPR.2019.00275",
        "project_url": "https://geometry.stanford.edu/projects/NOCS_CVPR2019/",
        "code_url": "https://github.com/hughw19/NOCS_CVPR2019",
        "authors": "He Wang, Srinath Sridhar, Jingwei Huang, Julien Valentin, Shuran Song, Leonidas J. Guibas",
        "venue": "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)",
        "year": "2019",
        "reading_status": "精读中",
        "desc_cn": "类别级 6D 位姿估计的奠基论文，把未知实例的位姿与尺寸估计统一到共享 canonical coordinate space。",
        "desc_en": "The foundational category-level 6D pose paper built around a shared canonical coordinate space.",
        "brief_cn": "它最关键的突破，不是把某个 benchmark 再提一点，而是把“同一类别里没见过的物体也能估位姿”变成了一个明确、可训练、可扩展的问题设定。",
        "brief_en": "Its key move is turning unseen-instance category-level pose estimation into a trainable canonical-space problem.",
        "one_line_cn": "如果你已经熟悉 DenseFusion 这类实例级方法，NOCS 值得读的地方就在于：它把输入从“某个已知物体”抬升成了“某一类未知物体”，让 6D 位姿估计开始真正讨论泛化。",
        "recommendation_cn": "当前库里已有 DenseFusion 和 FoundationPose，但还缺一篇真正代表“类别级位姿泛化”的奠基论文。NOCS 正好把实例级 pose 估计往 unseen instance、shared canonical space 和 mixed-reality data synthesis 这条线上补齐。",
        "recommendation_en": "The library already had instance-level and novel-object pose papers, but still lacked the foundational category-level pose generalization paper. NOCS fills that gap directly.",
        "influence_cn": "Semantic Scholar 检索页显示约 881 次引用；CVPR 2019 oral 级代表作，基本奠定了 category-level 6D pose estimation 的 NOCS 表达路线。",
        "innovation_cn": "它把机器人感知里的一个长期难点讲清楚了：很多抓取和操作系统并不缺 pose solver，而是缺“遇到没见过的杯子、瓶子、碗，还能给出稳定位姿”的统一表示。NOCS 给了这个问题第一套真正站得住的标准答案。",
        "innovation_en": "Its robotics value is giving manipulation systems a reusable way to reason about unseen object instances at the category level instead of assuming exact CAD identities.",
        "limitation_cn": "它仍依赖类别内共享几何先验，遇到类内形状差异很大、遮挡严重或 RGB-D 质量不足时会明显吃力；同时它更偏感知前端，不直接解决抓取质量与任务约束。",
        "limitation_en": "It still struggles when within-category shape variation or occlusion becomes too large, and it only addresses the perception front-end rather than grasp quality or task constraints.",
        "core_cn": [
            "提出 NOCS 作为同类别物体共享的 normalized object coordinate representation。",
            "在 Mask R-CNN 框架上同时预测类别、实例 mask 与像素级 NOCS correspondence。",
            "结合 RGB-D 深度信息恢复物体的 metric 6D pose 与尺寸，并引入 mixed-reality data synthesis 扩充训练集。",
        ],
        "core_en": [
            "Introduces NOCS as a shared normalized object coordinate representation across unseen instances in the same category.",
            "Builds on a region-based network that predicts category, mask, and pixel-wise NOCS correspondences jointly.",
            "Uses RGB-D depth to recover metric 6D pose and size, supported by context-aware mixed-reality data synthesis.",
        ],
        "terms": [
            ("category-level pose estimation", "类别级位姿估计"),
            ("NOCS", "归一化物体坐标空间"),
            ("canonical space", "规范坐标空间"),
            ("mixed reality synthesis", "混合现实数据合成"),
        ],
        "repro": [
            "先理解 NOCS map 与 instance-level CAD template 的区别，明确它为什么能支持 unseen instance。",
            "复查 Mask R-CNN 分支如何联合输出 mask、class 和 NOCS coordinate。",
            "重点看 mixed-reality data synthesis 与 REAL275 / CAMERA25 数据构成，它们后来成了很多类别级 pose 工作的默认起点。",
        ],
        "source_note": "来源组合：CVPR 2019 Open Access 页面与 PDF、arXiv 条目、Stanford 项目页、官方 GitHub、Semantic Scholar 引用页。",
        "topic_tokens": "6d pose estimation category-level pose estimation object pose estimation rgb-d pose perception manipulation",
        "search_tokens": "NOCS category-level 6D object pose size estimation canonical coordinate rgb-d pose perception REAL275 CAMERA25",
        "topic_badges": ["6d pose estimation", "category-level pose estimation", "object pose estimation", "rgb-d pose"],
        "english_pills": ["6D pose", "category-level", "RGB-D", "canonical space"],
    },
    {
        "title": "GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping",
        "slug": "graspnet-1billion",
        "pdf_url": "https://openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf",
        "arxiv_url": "https://arxiv.org/abs/1912.13470",
        "landing_url": "https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.html",
        "doi_url": "https://doi.org/10.1109/CVPR42600.2020.01146",
        "project_url": "https://graspnet.net/",
        "code_url": "https://github.com/graspnet/graspnet-baseline",
        "authors": "Hao-Shu Fang, Chenxi Wang, Minghao Gou, Cewu Lu",
        "venue": "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)",
        "year": "2020",
        "reading_status": "待复现",
        "desc_cn": "抓取方向最有代表性的公开 benchmark 之一，把真实 RGB-D clutter、密集抓取标注和统一评测正式结合起来。",
        "desc_en": "One of the most representative public grasping benchmarks, combining real RGB-D clutter with dense grasp annotations and a unified evaluation system.",
        "brief_cn": "它最有价值的地方不是“又多一个数据集”，而是把抓取研究从各做各的私有设定，推进到能在统一协议下比较 general object grasping。",
        "brief_en": "Its real contribution is not just scale, but standardizing general-object grasp evaluation across methods.",
        "one_line_cn": "如果 Dex-Net 代表“怎样学会抓”，GraspNet-1Billion 代表“怎样把抓取研究放到同一张公开考卷上做”。",
        "recommendation_cn": "当前库里已经有 Dex-Net 2.0 和 Contact-GraspNet，但还缺“为什么后来的 6-DoF grasp detection 能大规模比较、训练和迭代”的公共 benchmark 基座。GraspNet-1Billion 正好补这个结构位。",
        "recommendation_en": "The library already had classic grasp planning and 6-DoF grasp generation, but it still lacked the benchmark substrate that made large-scale grasp comparison and training practical.",
        "influence_cn": "Semantic Scholar 页面显示约 753 次引用；它不是单篇方法小改，而是把 general object grasping 的公开数据、评测协议和 baseline 一次性搭了起来。",
        "innovation_cn": "这篇论文最值得机器人实践者重视的一点，是它把“抓取 benchmark”从玩具级闭门评测，变成了真实 RGB-D clutter 场景里的公共基础设施。后续很多 grasp detection、graspness、foundation-assisted grasping 工作，本质上都在这个底座上往前推。",
        "innovation_en": "Its robotics contribution is making cluttered-scene RGB-D grasping a shared public infrastructure problem instead of a collection of isolated private setups.",
        "limitation_cn": "它主要聚焦双指抓取与数据/评测底座，本身不是任务级 grasping system；对多指灵巧手、语义条件抓取和复杂接触动力学的覆盖仍有限。",
        "limitation_en": "It is mainly a two-finger grasp benchmark and evaluation substrate, not a full task-level manipulation system or a multi-finger dexterous benchmark.",
        "core_cn": [
            "构建 97,280 张真实 RGB-D 图像、190 个 clutter scene、88 个物体和超过 10 亿抓取姿态的公开 benchmark。",
            "通过物体 6D pose 标注与解析抓取计算，把 object-level grasp pose 投影到 scene coordinate，降低密集抓取标注成本。",
            "提出统一评测协议与 baseline 网络，使不同 grasp pose 预测方法能在同一标准下比较。",
        ],
        "core_en": [
            "Builds a public benchmark with 97,280 real RGB-D images, 190 cluttered scenes, 88 objects, and over one billion grasp poses.",
            "Projects object-level grasp poses into scene coordinates using annotated object poses and analytic grasp computation.",
            "Provides a unified evaluation protocol and a baseline network for comparable grasp-pose prediction research.",
        ],
        "terms": [
            ("grasp pose detection", "抓取位姿检测"),
            ("cluttered scene", "杂乱场景"),
            ("grasp affinity field", "抓取亲和场"),
            ("benchmark protocol", "评测协议"),
        ],
        "repro": [
            "先看数据采集和 object pose annotation 流程，理解它为什么能大规模生成 scene-level grasp labels。",
            "读清 evaluation metric、pose-NMS 和 analytic success computation 的设计，不然很难正确比较后续方法。",
            "如果要做复现，优先从官方 baseline 和 graspnetAPI 入手，再看它与 Contact-GraspNet、AnyGrasp 系的接口差异。",
        ],
        "source_note": "来源组合：CVPR 2020 Open Access 页面与 PDF、GraspNet 官方项目页、baseline GitHub、Semantic Scholar 引用页。",
        "topic_tokens": "grasping grasp planning grasp detection 6-dof grasp benchmark rgb-d manipulation",
        "search_tokens": "GraspNet-1Billion general object grasping benchmark grasp pose detection cluttered scene rgb-d point cloud",
        "topic_badges": ["grasping", "grasp planning", "grasp detection", "benchmark"],
        "english_pills": ["grasping", "benchmark", "6-DoF grasp", "RGB-D"],
    },
]


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def safe_title_for_filename(title: str) -> str:
    cleaned = title.replace(":", " -")
    return re.sub(r'[<>"/\\\\|?*]', "_", cleaned)


def long_path(path: Path) -> str:
    raw = str(path.resolve())
    if raw.startswith("\\\\?\\"):
        return raw
    if len(raw) >= 240:
        return "\\\\?\\" + raw
    return raw


def ul(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{html.escape(item)}</li>" for item in items) + "</ul>"


def terms_grid(items: list[tuple[str, str]]) -> str:
    return "".join(
        f'<div class="term"><span class="en">{html.escape(en)}</span><br />{html.escape(cn)}</div>'
        for en, cn in items
    )


def download_pdf(paper: dict) -> None:
    file_name = f'{safe_title_for_filename(paper["title"])} - {TODAY}.pdf'
    desktop_path = DESKTOP_ROOT / file_name
    repo_path = WORKFLOW_ROOT / "papers" / file_name
    if not desktop_path.exists():
        urllib.request.urlretrieve(paper["pdf_url"], desktop_path)
    with open(long_path(desktop_path), "rb") as src, open(long_path(repo_path), "wb") as dst:
        shutil.copyfileobj(src, dst)
    paper["file_name"] = file_name
    paper["desktop_pdf_path"] = desktop_path
    paper["repo_pdf_path"] = repo_path
    paper["file_size_mb"] = round(desktop_path.stat().st_size / (1024 * 1024), 2)


def chinese_main_page(p1: dict, p2: dict) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>每日机器人论文对照</title>
  <style>
    :root {{
      --text:#2f373b; --muted:#6f787e; --line:#dce2e4; --bg:#f3f1eb; --page:#fffdf8;
      --blue:#2f5f9f; --steel:#7a8583; --grid:rgba(94,104,106,.052); --shadow:0 18px 50px rgba(34,42,46,.08);
    }}
    * {{ box-sizing:border-box; }}
    body {{
      margin:0;
      background:
        linear-gradient(90deg,var(--grid) 1px,transparent 1px),
        linear-gradient(0deg,var(--grid) 1px,transparent 1px),
        radial-gradient(circle at 8% 6%,rgba(255,255,255,.9),transparent 28%),
        radial-gradient(circle at 88% 9%,rgba(125,135,132,.13),transparent 25%),
        linear-gradient(180deg,#f8f6f0 0%,var(--bg) 46%,#eeece6 100%);
      background-size:30px 30px,30px 30px,auto,auto,auto;
      color:var(--text);
      font-family:"Microsoft YaHei UI","Microsoft YaHei","PingFang SC",sans-serif;
      line-height:1.82;
    }}
    .page {{
      position:relative; max-width:940px; margin:34px auto 54px; padding:58px 72px 78px;
      background:linear-gradient(180deg,rgba(255,253,248,.97) 0%,rgba(251,247,239,.94) 100%);
      border:1px solid var(--line); border-top:5px solid var(--steel); border-radius:10px;
      box-shadow:var(--shadow); overflow:hidden;
    }}
    h1 {{ margin:0 0 12px; font-size:36px; line-height:1.22; }}
    h2 {{ margin:42px 0 14px; padding-bottom:8px; border-bottom:1px solid var(--line); font-size:24px; }}
    h2::before {{ content:""; display:inline-block; width:8px; height:22px; margin-right:10px; vertical-align:-4px; background:var(--steel); border-radius:2px; }}
    h3 {{ margin:24px 0 8px; color:#5f6872; font-size:18px; }}
    p {{ margin:8px 0 16px; }}
    ul {{ margin:8px 0 16px 22px; padding:0; }}
    li {{ margin:4px 0; }}
    a {{ color:var(--blue); text-decoration:none; border-bottom:1px solid rgba(47,95,159,.24); }}
    .subtitle {{ margin:0 0 12px; color:#4b5563; font-size:17px; font-weight:600; line-height:1.7; }}
    .meta,.local {{ color:var(--muted); font-size:14px; overflow-wrap:anywhere; }}
    .top-actions,.actions {{ display:flex; flex-wrap:wrap; gap:10px; margin:14px 0 18px; }}
    .btn {{
      display:inline-flex; align-items:center; justify-content:center; min-height:38px; padding:8px 14px;
      border-radius:7px; background:linear-gradient(180deg,#202a33,#151b22); color:#fff; border:1px solid #151b22;
      box-shadow:0 8px 18px rgba(21,27,34,.12); font-size:14px; font-weight:700; text-decoration:none;
    }}
    .btn.secondary {{ background:rgba(255,255,255,.76); color:var(--text); border-color:var(--line); box-shadow:none; }}
    .callout {{
      margin:22px 0; padding:16px 18px; background:rgba(255,250,242,.82); border:1px solid #ece8dd;
      border-left:4px solid #a4aaa6; border-radius:8px;
    }}
    .today-grid {{ display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:12px; margin:20px 0 28px; }}
    .today-card {{
      padding:14px 15px; background:rgba(255,255,255,.74); border:1px solid var(--line); border-radius:8px;
      color:#47515a; font-size:14px; box-shadow:0 10px 28px rgba(34,42,46,.055);
    }}
    .today-card strong {{ display:block; color:var(--text); margin-bottom:4px; }}
    .paper-title {{ font-size:20px; font-weight:700; }}
    .en {{ font-family:"Times New Roman",Times,serif; }}
    .tag {{ display:inline-block; margin-right:8px; padding:3px 9px; border-radius:999px; background:#f7f9f8; border:1px solid #e7ecec; color:#4b5563; font-size:13px; }}
    @media (max-width:900px) {{ .today-grid {{ grid-template-columns:repeat(2,minmax(0,1fr)); }} }}
    @media (max-width:720px) {{ .page {{ padding:40px 22px 52px; }} .today-grid {{ grid-template-columns:1fr; }} }}
  </style>
</head>
<body>
  <main class="page">
    <h1>每日机器人论文对照</h1>
    <p class="subtitle">今日创新点：今天这组更像是在补机器人操作里最容易被割裂的两层能力。一层是“同类但没见过的物体，位姿到底怎么稳健估出来”；另一层是“有了感知之后，抓取研究怎样在统一公开协议下做规模化比较和训练”。</p>
    <p class="subtitle">未来创新点：下一步最值得追的是把 NOCS 这类 category-level pose 表达，与 GraspNet 这类 clutter grasp benchmark 结合起来，再往上接语言条件抓取、foundation-model-assisted grasping 和任务级执行闭环。</p>
    <div class="meta">更新时间：{TODAY} · 今日论文：{TODAY} 追加刷新</div>
    <div class="top-actions"><a class="btn secondary" href="./robotics-paper-feishu-page-en.html">English Translation</a></div>
    <p class="local">论文库地址：<a href="./paper-folder-index.html">./paper-folder-index.html</a></p>

    <div class="callout">
      今日主题：用一篇 category-level 6D pose 奠基论文，对照一篇通用抓取 benchmark 奠基论文，补足当前论文库在“类别泛化感知 / 抓取公共基座 / 感知到操作接口”上的结构空位。
    </div>

    <section class="today-grid" aria-label="今日重点总览">
      <div class="today-card"><strong>先读顺序</strong>先读 NOCS，先把“未知实例的类别级位姿估计”想清楚；再读 GraspNet-1Billion，看抓取研究为什么需要统一 benchmark。</div>
      <div class="today-card"><strong>关键词</strong>category-level pose estimation、NOCS、RGB-D pose、general object grasping、6-DoF grasp、benchmark</div>
      <div class="today-card"><strong>今日追问</strong>如果未来要做 foundation-model-assisted grasping，底层到底更缺“更强的类别级 pose 表达”，还是“更强的公开 grasp 评测与数据闭环”？</div>
      <div class="today-card"><strong>影响力依据</strong>NOCS 在 Semantic Scholar 约 881 次引用；GraspNet-1Billion 约 753 次引用，都是各自子方向的代表底座。</div>
      <div class="today-card"><strong>互补性</strong>前者解决“同类未知物体怎么看准”，后者解决“抓取方法如何在真实 clutter 里标准化比较”。</div>
    </section>

    <h2 id="{p1["slug"]}">论文 1</h2>
    <p class="paper-title en">{html.escape(p1["title"])}（{TODAY}）</p>
    <p>论文链接：<a href="{p1["arxiv_url"]}">{p1["arxiv_url"]}</a> · DOI：<a href="{p1["doi_url"]}">{p1["doi_url"].replace("https://doi.org/","")}</a></p>
    <div class="actions">
      <a class="btn" href="./papers/{html.escape(p1["file_name"])}">打开 PDF</a>
      <a class="btn secondary" href="./paper-folder-index.html">论文库</a>
      <a class="btn secondary" href="./translations/{p1["slug"]}.html">查看分析结果</a>
      <a class="btn secondary" href="{p1["arxiv_url"]}">arXiv</a>
    </div>
    <p><span class="tag">category-level pose estimation</span><span class="tag">6D pose estimation</span><span class="tag">RGB-D pose</span><span class="tag">canonical space</span></p>
    <h3>两篇论文介绍</h3>
    <p>{html.escape(p1["desc_cn"])}</p>
    <h3>核心方法</h3>
    {ul(p1["core_cn"])}
    <h3>我认为的机器人创新点</h3>
    <p>{html.escape(p1["innovation_cn"])}</p>
    <h3>局限</h3>
    <p>{html.escape(p1["limitation_cn"])}</p>

    <h2 id="{p2["slug"]}">论文 2</h2>
    <p class="paper-title en">{html.escape(p2["title"])}（{TODAY}）</p>
    <p>论文链接：<a href="{p2["arxiv_url"]}">{p2["arxiv_url"]}</a> · DOI：<a href="{p2["doi_url"]}">{p2["doi_url"].replace("https://doi.org/","")}</a></p>
    <div class="actions">
      <a class="btn" href="./papers/{html.escape(p2["file_name"])}">打开 PDF</a>
      <a class="btn secondary" href="./paper-folder-index.html">论文库</a>
      <a class="btn secondary" href="./translations/{p2["slug"]}.html">查看分析结果</a>
      <a class="btn secondary" href="{p2["arxiv_url"]}">arXiv</a>
    </div>
    <p><span class="tag">grasping</span><span class="tag">benchmark</span><span class="tag">grasp detection</span><span class="tag">RGB-D clutter</span></p>
    <h3>两篇论文介绍</h3>
    <p>{html.escape(p2["desc_cn"])}</p>
    <h3>核心方法</h3>
    {ul(p2["core_cn"])}
    <h3>我认为的机器人创新点</h3>
    <p>{html.escape(p2["innovation_cn"])}</p>
    <h3>局限</h3>
    <p>{html.escape(p2["limitation_cn"])}</p>

    <h2>对比结论</h2>
    <p><strong>NOCS</strong> 更偏“把物体看准”，而且是把 pose estimation 从实例级推向类别级泛化。</p>
    <p><strong>GraspNet-1Billion</strong> 更偏“把抓取研究放到统一公开底座上比较”，它不直接替你抓，但决定了后续很多 grasp detection 方法怎么被训练、评测和迭代。</p>
    <p>这组一起看，能把当前论文库里“位姿感知”和“抓取 benchmark”之间缺掉的那一段补上。</p>

    <h3>阅读顺序</h3>
    <p>先读 <span class="en">NOCS</span>，再读 <span class="en">GraspNet-1Billion</span>。</p>
  </main>
</body>
</html>
"""


def english_main_page(p1: dict, p2: dict) -> str:
    desktop_uri = DESKTOP_ROOT.as_posix()
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Daily Robotics Paper Briefing</title>
  <style>
    :root {{ --text:#30363a; --muted:#747b82; --line:#dee0e3; --bg:#f4f3ee; --blue:#245bdb; --steel:#7b8580; --grid:rgba(123,133,128,.045); --warm:#fff8ec; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:linear-gradient(90deg,var(--grid) 1px,transparent 1px),linear-gradient(0deg,var(--grid) 1px,transparent 1px),radial-gradient(circle at 12% 0%,rgba(255,250,242,.8),transparent 30%),var(--bg); background-size:30px 30px,30px 30px,auto,auto; color:var(--text); font-family:"Microsoft YaHei UI","Microsoft YaHei","PingFang SC",sans-serif; line-height:1.82; }}
    .page {{ max-width:900px; margin:32px auto; padding:58px 72px 76px; background:linear-gradient(180deg,#fff 0%,var(--warm) 100%); border:1px solid #cfd5dc; border-top:5px solid var(--steel); box-shadow:0 18px 42px rgba(31,35,41,.08); }}
    h1 {{ margin:0 0 12px; font-size:34px; line-height:1.25; }}
    h2 {{ margin:42px 0 14px; padding-bottom:8px; border-bottom:1px solid var(--line); font-size:24px; }}
    h2::before {{ content:""; display:inline-block; width:8px; height:22px; margin-right:10px; vertical-align:-4px; background:var(--steel); border-radius:2px; }}
    h3 {{ margin:26px 0 8px; color:#8f5f52; font-size:18px; }}
    p {{ margin:8px 0 16px; }}
    ul {{ margin:8px 0 16px 22px; padding:0; }}
    a {{ color:var(--blue); text-decoration:none; border-bottom:1px solid rgba(36,91,219,.28); }}
    .subtitle {{ margin:0 0 14px; color:#4b5563; font-size:17px; font-weight:600; }}
    .meta,.local {{ color:var(--muted); font-size:14px; overflow-wrap:anywhere; }}
    .callout {{ margin:22px 0; padding:14px 16px; background:#fff7eb; border-left:4px solid #a4aaa6; border-radius:6px; }}
    .today-grid {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; margin:20px 0 28px; }}
    .today-card {{ padding:14px 15px; background:#fff; border:1px solid var(--line); border-radius:8px; font-size:14px; color:#4b5563; }}
    .today-card strong {{ display:block; color:var(--text); margin-bottom:4px; }}
    .paper-title {{ font-family:"Times New Roman",Times,serif; font-size:20px; font-weight:700; }}
    .tag {{ display:inline-block; margin-right:8px; padding:2px 8px; border-radius:6px; background:#eef1f4; border:1px solid #d7dde4; color:#4b5563; font-size:13px; }}
    .actions,.top-actions {{ display:flex; flex-wrap:wrap; gap:10px; margin:14px 0 18px; }}
    .btn {{ display:inline-flex; align-items:center; justify-content:center; min-height:36px; padding:7px 13px; border-radius:6px; background:#1f2329; color:#fff; border:1px solid #1f2329; font-size:14px; font-weight:700; text-decoration:none; }}
    .btn.secondary {{ background:#fff; color:var(--text); border-color:var(--line); }}
    @media (max-width:760px) {{ .page {{ padding:40px 22px 52px; }} .today-grid {{ grid-template-columns:1fr; }} }}
  </style>
</head>
<body>
  <main class="page">
    <h1>Daily Robotics Paper Briefing</h1>
    <p class="subtitle">Today’s innovation point: this pair repairs a common split in robotics manipulation stacks. One paper asks how to estimate pose for unseen instances within a category; the other asks how grasping research becomes comparable and scalable under a public benchmark.</p>
    <p class="subtitle">Next innovation point: connect category-level pose representations such as NOCS with GraspNet-style clutter grasp benchmarks, then push upward toward language-conditioned and foundation-assisted grasping loops.</p>
    <div class="meta">Updated: {TODAY} · appended daily refresh</div>
    <div class="top-actions"><a class="btn secondary" href="robotics-paper-feishu-page.html">返回中文</a></div>
    <p class="local">Paper library: <a href="file:///{desktop_uri}/index.html">file:///{desktop_uri}/index.html</a></p>
    <div class="callout">Today’s pair is intentionally complementary: NOCS expands 6D pose estimation from instance-level recognition to category-level generalization, while GraspNet-1Billion provides the public grasp benchmark substrate that later clutter-grasping systems build on.</div>
    <section class="today-grid">
      <div class="today-card"><strong>Read First</strong>Read NOCS first, then GraspNet-1Billion.</div>
      <div class="today-card"><strong>Keywords</strong>category-level pose, NOCS, RGB-D pose, grasp benchmark, grasp detection, clutter.</div>
      <div class="today-card"><strong>Impact</strong>Semantic Scholar counts are about 881 for NOCS and 753 for GraspNet-1Billion.</div>
      <div class="today-card"><strong>Complement</strong>Generalized pose perception versus benchmark infrastructure for grasping.</div>
    </section>
    <h2 id="{p1["slug"]}">Paper 1</h2>
    <p class="paper-title">{html.escape(p1["title"])} ({TODAY})</p>
    <p>Links: <a href="{p1["arxiv_url"]}">arXiv</a> · DOI: <a href="{p1["doi_url"]}">{p1["doi_url"].replace("https://doi.org/","")}</a></p>
    <div class="actions">
      <a class="btn" href="file:///{p1["desktop_pdf_path"].as_posix()}">Open PDF</a>
      <a class="btn secondary" href="file:///{desktop_uri}/index.html">Paper Library</a>
      <a class="btn secondary" href="file:///{desktop_uri}/translations/{p1["slug"]}.html">View Analysis</a>
      <a class="btn secondary" href="{p1["arxiv_url"]}">arXiv</a>
    </div>
    <p><span class="tag">category-level pose</span><span class="tag">RGB-D</span><span class="tag">perception</span><span class="tag">canonical space</span></p>
    <h3>Why It Was Chosen</h3>
    <p>{html.escape(p1["recommendation_en"])}</p>
    <h3>Core Methods</h3>
    {ul(p1["core_en"])}
    <h3>Robotics Insight</h3>
    <p>{html.escape(p1["innovation_en"])}</p>
    <h3>Main Limitation</h3>
    <p>{html.escape(p1["limitation_en"])}</p>

    <h2 id="{p2["slug"]}">Paper 2</h2>
    <p class="paper-title">{html.escape(p2["title"])} ({TODAY})</p>
    <p>Links: <a href="{p2["arxiv_url"]}">arXiv</a> · DOI: <a href="{p2["doi_url"]}">{p2["doi_url"].replace("https://doi.org/","")}</a></p>
    <div class="actions">
      <a class="btn" href="file:///{p2["desktop_pdf_path"].as_posix()}">Open PDF</a>
      <a class="btn secondary" href="file:///{desktop_uri}/index.html">Paper Library</a>
      <a class="btn secondary" href="file:///{desktop_uri}/translations/{p2["slug"]}.html">View Analysis</a>
      <a class="btn secondary" href="{p2["arxiv_url"]}">arXiv</a>
    </div>
    <p><span class="tag">grasping</span><span class="tag">benchmark</span><span class="tag">6-DoF grasp</span><span class="tag">RGB-D clutter</span></p>
    <h3>Why It Was Chosen</h3>
    <p>{html.escape(p2["recommendation_en"])}</p>
    <h3>Core Methods</h3>
    {ul(p2["core_en"])}
    <h3>Robotics Insight</h3>
    <p>{html.escape(p2["innovation_en"])}</p>
    <h3>Main Limitation</h3>
    <p>{html.escape(p2["limitation_en"])}</p>

    <h2>Comparison</h2>
    <p><strong>NOCS</strong> is about expanding pose estimation from known instances to unseen objects within a category.</p>
    <p><strong>GraspNet-1Billion</strong> is about making grasp research comparable, reproducible, and scalable under one public clutter benchmark.</p>
    <p>Read them in that order to connect generalized pose perception with the benchmark substrate that later grasping systems stand on.</p>
  </main>
</body>
</html>
"""


def translation_page(paper: dict, library_href: str, pdf_href: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{paper["slug"]} 论文导读</title>
  <style>
    :root {{
      --bg:#f3f1eb; --text:#2f373b; --muted:#6f787e; --line:#dce2e4; --steel:#7a8583;
      --blue:#2f5f9f; --shadow:0 18px 50px rgba(34,42,46,.08); --grid:rgba(94,104,106,.052);
    }}
    * {{ box-sizing:border-box; }}
    body {{
      margin:0; min-height:100vh; color:var(--text);
      background:
        radial-gradient(circle at 8% 6%,rgba(255,255,255,.9),transparent 28%),
        linear-gradient(90deg,var(--grid) 1px,transparent 1px),
        linear-gradient(0deg,var(--grid) 1px,transparent 1px),
        linear-gradient(180deg,#f8f6f0 0%,var(--bg) 48%,#eeece6 100%);
      background-size:auto,30px 30px,30px 30px,auto;
      font-family:"Microsoft YaHei UI","Microsoft YaHei","PingFang SC",sans-serif;
      line-height:1.86;
    }}
    main {{
      width:min(920px,calc(100% - 36px)); margin:34px auto 54px; padding:48px 60px 64px;
      background:linear-gradient(180deg,rgba(255,253,248,.97),rgba(251,247,239,.94));
      border:1px solid var(--line); border-top:5px solid var(--steel); border-radius:10px;
      box-shadow:var(--shadow);
    }}
    h1 {{ margin:0 0 10px; font-size:32px; line-height:1.25; }}
    h2 {{ margin:34px 0 12px; padding-bottom:7px; border-bottom:1px solid var(--line); font-size:24px; }}
    p {{ margin:8px 0 16px; }}
    ul {{ margin:8px 0 16px 22px; padding:0; }}
    a {{ color:var(--blue); text-decoration:none; border-bottom:1px solid rgba(47,95,159,.25); }}
    .en {{ font-family:"Times New Roman",Times,serif; }}
    .meta,.note {{ color:var(--muted); font-size:14px; }}
    .actions {{ display:flex; flex-wrap:wrap; gap:10px; margin:18px 0 20px; }}
    .btn {{
      display:inline-flex; align-items:center; justify-content:center; min-height:38px; padding:8px 14px;
      border-radius:7px; background:linear-gradient(180deg,#202a33,#151b22); color:white;
      border:1px solid #151b22; font-weight:700; text-decoration:none;
    }}
    .btn.secondary {{ background:rgba(255,255,255,.76); color:var(--text); border-color:var(--line); }}
    .callout {{
      margin:20px 0; padding:16px 17px; background:rgba(255,250,242,.82); border:1px solid #ece8dd;
      border-left:4px solid #a4aaa6; border-radius:8px;
    }}
    .terms {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px; }}
    .term {{ padding:12px 13px; background:rgba(255,255,255,.74); border:1px solid var(--line); border-radius:8px; }}
    @media (max-width:760px) {{ main {{ padding:28px 22px 40px; }} .terms {{ grid-template-columns:1fr; }} }}
  </style>
</head>
<body>
  <main>
    <p class="meta">论文导读 · {TODAY} · 阅读状态：{paper["reading_status"]}</p>
    <h1><span class="en">{html.escape(paper["title"])}</span>：{html.escape(paper["desc_cn"])}</h1>
    <p class="note">建议把它和今天另一篇论文对照着读，重点看它补的是哪一层机器人能力。</p>
    <div class="actions">
      <a class="btn" href="{pdf_href}">打开原文 PDF</a>
      <a class="btn secondary" href="{library_href}">返回论文库</a>
      <a class="btn secondary" href="{paper["arxiv_url"]}">arXiv</a>
      <a class="btn secondary" href="{paper["doi_url"]}">DOI</a>
    </div>
    <div class="callout"><strong>一句话导读：</strong>{html.escape(paper["one_line_cn"])}</div>
    <h2>英文信息</h2>
    <p><strong>标题：</strong><span class="en">{html.escape(paper["title"])}</span></p>
    <p><strong>作者：</strong><span class="en">{html.escape(paper["authors"])}</span></p>
    <p><strong>发表：</strong>{html.escape(paper["venue"])}，{paper["year"]}</p>
    <p><strong>DOI：</strong><a href="{paper["doi_url"]}">{paper["doi_url"].replace("https://doi.org/","")}</a></p>
    <p><strong>arXiv：</strong><a href="{paper["arxiv_url"]}">{paper["arxiv_url"].replace("https://arxiv.org/abs/","")}</a></p>
    <p><strong>项目 / 代码：</strong><a href="{paper["project_url"]}">{paper["project_url"]}</a> · <a href="{paper["code_url"]}">{paper["code_url"]}</a></p>
    <p><strong>原文页面：</strong><a href="{paper["landing_url"]}">{paper["landing_url"]}</a></p>
    <h2>术语对照</h2>
    <div class="terms">{terms_grid(paper["terms"])}</div>
    <h2>中文导读</h2>
    <p>{html.escape(paper["brief_cn"])}</p>
    <p>{html.escape(paper["recommendation_cn"])}</p>
    <h2>推荐理由</h2>
    <p>{html.escape(paper["recommendation_cn"])}</p>
    <h2>引用 / 影响力说明</h2>
    <p>{html.escape(paper["influence_cn"])}</p>
    <h2>复现清单</h2>
    {ul(paper["repro"])}
    <h2>论文来源</h2>
    <p>{html.escape(paper["source_note"])}</p>
    <h2>卡片元数据</h2>
    <p><strong>方向：</strong>{html.escape(paper["topic_tokens"].replace(" ", " / "))}</p>
    <p><strong>文件名：</strong><span class="en">{html.escape(paper["file_name"])}</span></p>
    <p><strong>推荐标签：</strong>{html.escape("、".join(paper["topic_badges"]))}</p>
  </main>
</body>
</html>
"""


def chinese_article_block(paper: dict, index_number: int, analysis_href: str) -> str:
    options = []
    for value in ["已导读", "精读中", "待复现", "已复现", "暂存"]:
        selected = " selected" if value == paper["reading_status"] else ""
        options.append(f'<option value="{value}"{selected}>{value}</option>')
    pills = "".join(f'<span class="pill">{html.escape(badge)}</span>' for badge in paper["topic_badges"])
    return f"""
      <article class="paper" data-id="{paper["slug"]}-{TODAY}" data-status="{paper["reading_status"]}" data-topic="{paper["topic_tokens"]}" data-search="{paper["search_tokens"]}">
        <span class="badge">论文 {index_number} · {TODAY}</span>
        <h2 class="title">{html.escape(paper["title"])}</h2>
        <p class="desc">{html.escape(paper["desc_cn"])}</p>
        <div class="brief"><strong>内容介绍：</strong>{html.escape(paper["brief_cn"])}</div>
        <div class="meta"><label class="status-control">状态<select class="status-editor" aria-label="修改 {paper["slug"]} 阅读状态">{"".join(options)}</select></label>{pills}<span class="pill">{paper["file_size_mb"]} MB</span></div>
        <div class="actions"><a class="btn" href="{html.escape(paper["file_name"])}">打开 PDF</a><a class="btn secondary" href="{analysis_href}">查看分析结果</a><a class="btn secondary" href="{paper["arxiv_url"]}">arXiv</a></div>
      </article>
"""


def english_article_block(paper: dict, index_number: int, analysis_href: str, pdf_href: str) -> str:
    return (
        f'<article class="paper"><span class="badge">Paper {index_number} · {TODAY}</span>'
        f'<h2 class="title">{html.escape(paper["title"])}</h2>'
        f'<p class="desc">{html.escape(paper["desc_en"])}</p>'
        f'<div class="brief"><strong>Summary:</strong> {html.escape(paper["brief_en"])}</div>'
        f'<div class="meta"><span class="pill">{paper["file_size_mb"]} MB</span><span class="pill">{html.escape(paper["english_pills"][0])}</span></div>'
        f'<div class="actions"><a class="btn" href="{pdf_href}">Open PDF</a><a class="btn secondary" href="{analysis_href}">View Analysis</a><a class="btn secondary" href="{paper["arxiv_url"]}">arXiv</a></div></article>'
    )


def update_chinese_library(path: Path, analysis_mode: str) -> None:
    content = path.read_text(encoding="utf-8")
    articles = re.findall(r'(?s)<article class="paper".*?</article>', content)
    for article_index, article in enumerate(list(articles), start=1):
        for paper in PAPERS:
            if paper["title"] in article:
                analysis_href = (
                    f"translations/{paper['slug']}.html"
                    if analysis_mode == "outputs"
                    else f"../index.html#{paper['slug']}"
                )
                articles[article_index - 1] = chinese_article_block(paper, article_index, analysis_href)
                break

    joined = "".join(articles)
    for paper in PAPERS:
        if paper["title"] not in joined:
            index_number = len(articles) + 1
            analysis_href = (
                f"translations/{paper['slug']}.html"
                if analysis_mode == "outputs"
                else f"../index.html#{paper['slug']}"
            )
            articles.append(chinese_article_block(paper, index_number, analysis_href))
            joined = "".join(articles)

    new_panel = """
    <section class="panel">
      <h2>今日重点</h2>
      <div class="overview">
        <div class="overview-card"><strong>先读建议：</strong>先看 NOCS，把“同类未知实例为什么还能估位姿”想清楚；再读 GraspNet-1Billion，看抓取研究为什么必须有统一公开 benchmark。</div>
        <div class="overview-card"><strong>研究抓手：</strong>今天补的是“category-level 6D pose + general object grasp benchmark”这段底座。它把当前论文库从实例级 pose、novel-object pose 和 grasp method，继续往更底层的公共基础设施补全。</div>
      </div>
      <div class="controls" aria-label="搜索与筛选">
        <input id="searchBox" type="search" placeholder="搜索标题、标签、方向，例如 grasp / pose / category-level / clutter / RGB-D" />
        <select id="statusFilter">
          <option value="all">全部状态</option>
          <option value="精读中">精读中</option>
          <option value="待复现">待复现</option>
          <option value="已导读">已导读</option>
          <option value="已复现">已复现</option>
          <option value="暂存">暂存</option>
        </select>
        <select id="topicFilter">
          <option value="all">全部方向</option>
          <option value="robot dynamics">robot dynamics</option>
          <option value="sim-to-real">sim-to-real</option>
          <option value="world model">world model</option>
          <option value="benchmark">benchmark</option>
          <option value="vla">VLA</option>
          <option value="policy improvement">policy improvement</option>
          <option value="mobile manipulation">mobile manipulation</option>
          <option value="slam">SLAM</option>
          <option value="perception">perception</option>
          <option value="diffusion policy">diffusion policy</option>
          <option value="6d pose estimation">6d pose estimation</option>
          <option value="category-level pose estimation">category-level pose estimation</option>
          <option value="object pose estimation">object pose estimation</option>
          <option value="rgb-d pose">rgb-d pose</option>
          <option value="foundation-model-assisted pose">foundation-model-assisted pose</option>
          <option value="grasping">grasping</option>
          <option value="grasp planning">grasp planning</option>
          <option value="grasp detection">grasp detection</option>
          <option value="grasp quality prediction">grasp quality prediction</option>
        </select>
        <select id="pageSize">
          <option value="2">每页 2 篇</option>
          <option value="4">每页 4 篇</option>
          <option value="8">每页 8 篇</option>
        </select>
      </div>
    </section>
"""

    content = re.sub(
        r'(?s)<section class="panel">.*?</section>\s*<section class="grid" id="paperGrid">',
        new_panel + '\n\n    <section class="grid" id="paperGrid">',
        content,
    )
    content = re.sub(
        r'(?s)<section class="grid" id="paperGrid">.*?</section>\s*<nav class="pagination"',
        '<section class="grid" id="paperGrid">\n' + "\n".join(articles) + '\n    </section>\n\n    <nav class="pagination"',
        content,
    )
    content = re.sub(r"当前日期：\d{4}-\d{2}-\d{2} · 累计收录 \d+ 篇", f"当前日期：{TODAY} · 累计收录 {len(articles)} 篇", content)
    content = re.sub(
        r"libraryCount\.textContent = `当前日期：\d{4}-\d{2}-\d{2} · 累计收录 \$\{papers\.length\} 篇`;",
        f"libraryCount.textContent = `当前日期：{TODAY} · 累计收录 ${{papers.length}} 篇`;",
        content,
    )
    path.write_text(content, encoding="utf-8")


def update_english_library(path: Path, outputs_mode: bool) -> None:
    content = path.read_text(encoding="utf-8")
    articles = re.findall(r'(?s)<article class="paper">.*?</article>', content)
    for article_index, article in enumerate(list(articles), start=1):
        for paper in PAPERS:
            if paper["title"] in article:
                analysis_href = (
                    f"file:///{DESKTOP_ROOT.as_posix()}/translations/{paper['slug']}.html"
                    if outputs_mode
                    else f"../index-en.html#{paper['slug']}"
                )
                articles[article_index - 1] = english_article_block(paper, article_index, analysis_href, paper["file_name"])
                break

    joined = "".join(articles)
    for paper in PAPERS:
        if paper["title"] not in joined:
            index_number = len(articles) + 1
            analysis_href = (
                f"file:///{DESKTOP_ROOT.as_posix()}/translations/{paper['slug']}.html"
                if outputs_mode
                else f"../index-en.html#{paper['slug']}"
            )
            articles.append(english_article_block(paper, index_number, analysis_href, paper["file_name"]))
            joined = "".join(articles)

    folder_href = f"file:///{DESKTOP_ROOT.as_posix()}/" if outputs_mode else "./"
    content = re.sub(
        r'(?s)<div class="toolbar"><span>Date: .*?</span><a class="open-folder".*?</div>',
        f'<div class="toolbar"><span>Date: {TODAY} · {len(articles)} papers</span><a class="open-folder" href="{folder_href}">Open folder</a></div>',
        content,
    )
    filters = '<section class="filters"><span class="filter">manipulation</span><span class="filter">benchmark</span><span class="filter">VLA</span><span class="filter">SLAM</span><span class="filter">perception</span><span class="filter">6D pose</span><span class="filter">novel object</span><span class="filter">category-level pose</span><span class="filter">grasping</span><span class="filter">grasp benchmark</span></section>'
    content = re.sub(r'(?s)<section class="filters">.*?</section>\s*<section class="grid">', filters + '\n    <section class="grid">', content)
    content = re.sub(r'(?s)<section class="grid">.*?</section>\s*</main>', '<section class="grid">' + "".join(articles) + '</section>\n  </main>', content)
    path.write_text(content, encoding="utf-8")


def update_launcher(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    content = content.replace(
        '$dexTranslationPath = Join-Path $libraryRoot "translations\\dexsim2real.html"',
        '$firstAnalysisPath = Join-Path $libraryRoot "translations\\nocs.html"',
    )
    content = content.replace(
        '$roboTranslationPath = Join-Path $libraryRoot "translations\\robowm-bench.html"',
        '$secondAnalysisPath = Join-Path $libraryRoot "translations\\graspnet-1billion.html"',
    )
    content = content.replace("Open DexSim2Real translation", "Open NOCS analysis")
    content = content.replace("Open RoboWM-Bench translation", "Open GraspNet-1Billion analysis")
    content = content.replace(
        '$openDexTranslation.Add_Click({ if (Test-Path $dexTranslationPath) { Start-Process -FilePath $dexTranslationPath } })',
        '$openDexTranslation.Add_Click({ if (Test-Path $firstAnalysisPath) { Start-Process -FilePath $firstAnalysisPath } })',
    )
    content = content.replace(
        '$openRoboTranslation.Add_Click({ if (Test-Path $roboTranslationPath) { Start-Process -FilePath $roboTranslationPath } })',
        '$openRoboTranslation.Add_Click({ if (Test-Path $secondAnalysisPath) { Start-Process -FilePath $secondAnalysisPath } })',
    )
    path.write_text(content, encoding="utf-8")


def main() -> None:
    ensure_dir(DESKTOP_ROOT)
    ensure_dir(DESKTOP_ROOT / "translations")
    ensure_dir(WORKFLOW_ROOT / "papers")
    ensure_dir(WORKFLOW_ROOT / "papers" / "translations")
    ensure_dir(OUTPUTS_ROOT / "translations")

    for paper in PAPERS:
        download_pdf(paper)

    cn_main = chinese_main_page(PAPERS[0], PAPERS[1])
    en_main = english_main_page(PAPERS[0], PAPERS[1])
    (OUTPUTS_ROOT / "robotics-paper-feishu-page.html").write_text(cn_main, encoding="utf-8")
    (WORKFLOW_ROOT / "index.html").write_text(cn_main, encoding="utf-8")
    (OUTPUTS_ROOT / "robotics-paper-feishu-page-en.html").write_text(en_main, encoding="utf-8")
    (WORKFLOW_ROOT / "index-en.html").write_text(en_main, encoding="utf-8")

    for paper in PAPERS:
        output_translation = translation_page(paper, "../paper-folder-index.html", f"../{paper['file_name']}")
        repo_translation = translation_page(paper, "../index.html", f"../{paper['file_name']}")
        (OUTPUTS_ROOT / "translations" / f"{paper['slug']}.html").write_text(output_translation, encoding="utf-8")
        (WORKFLOW_ROOT / "papers" / "translations" / f"{paper['slug']}.html").write_text(repo_translation, encoding="utf-8")

    update_chinese_library(OUTPUTS_ROOT / "paper-folder-index.html", "outputs")
    update_chinese_library(WORKFLOW_ROOT / "papers" / "index.html", "repo")
    update_english_library(OUTPUTS_ROOT / "paper-folder-index-en.html", True)
    update_english_library(WORKFLOW_ROOT / "papers" / "index-en.html", False)
    update_launcher(WORKFLOW_ROOT / "scripts" / "robot-paper-dynamic-launcher.ps1")

    shutil.copy2(OUTPUTS_ROOT / "paper-folder-index.html", DESKTOP_ROOT / "index.html")
    shutil.copy2(OUTPUTS_ROOT / "paper-folder-index-en.html", DESKTOP_ROOT / "index-en.html")
    shutil.copytree(OUTPUTS_ROOT / "translations", DESKTOP_ROOT / "translations", dirs_exist_ok=True)


if __name__ == "__main__":
    main()
