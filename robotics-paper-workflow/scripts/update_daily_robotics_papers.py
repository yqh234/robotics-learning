from __future__ import annotations

import html
import re
import shutil
import urllib.request
from pathlib import Path


ROOT = Path(r"C:\Users\86136\Documents\Codex\2026-06-15\codex-codex")
REPO_ROOT = ROOT / "work" / "robotics-learning"
WORKFLOW_ROOT = REPO_ROOT / "robotics-paper-workflow"
OUTPUTS_ROOT = ROOT / "outputs"
DESKTOP_ROOT = Path(r"C:\Users\86136\Desktop\机器人论文 PDFs")
TODAY = "2026-06-22"


PAPERS = [
    {
        "title": "PoseCNN: A Convolutional Neural Network for 6D Object Pose Estimation in Cluttered Scenes",
        "slug": "posecnn",
        "pdf_url": "https://www.roboticsproceedings.org/rss14/p19.pdf",
        "arxiv_url": "https://arxiv.org/abs/1711.00199",
        "landing_url": "https://www.roboticsproceedings.org/rss14/p19.html",
        "doi_url": "https://doi.org/10.15607/RSS.2018.XIV.019",
        "project_url": "https://rse-lab.cs.washington.edu/projects/posecnn/",
        "code_url": "https://github.com/yuxng/PoseCNN",
        "extra_url": "https://github.com/yuxng/YCB_Video_toolbox",
        "authors": "Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, Dieter Fox",
        "venue": "Robotics: Science and Systems (RSS)",
        "year": "2018",
        "reading_status": "精读中",
        "desc_cn": "经典 6D 位姿估计代表作，用 RGB 图像先把物体中心、距离和旋转拆开估，再在遮挡和对称物体场景里稳住结果。",
        "desc_en": "A landmark RGB-first 6D pose paper for cluttered manipulation scenes.",
        "brief_cn": "这篇论文的历史价值不只是“早期深度学习位姿估计”。它真正留下来的，是一套后来很多方法都绕不开的问题定义：在杂乱、遮挡、对称物体条件下，怎样把已知物体的 6D 位姿估计做成可训练、可复现、可比较的视觉模块。",
        "brief_en": "Its lasting value is not just being early. It helped define the modern learned known-object 6D pose pipeline under clutter, occlusion, and symmetry.",
        "one_line_cn": "如果说 DenseFusion 把 RGB-D 融合推进到了一个更强阶段，那 PoseCNN 值得先读，因为很多后来的对比、数据集和误差口径，都是从它这里真正立住的。",
        "recommendation_cn": "当前论文库已经有 DenseFusion、FoundationPose、NOCS 这几类更后续的工作，但还缺一篇真正奠定“已知物体、RGB 主导、遮挡鲁棒、对称处理、YCB-Video 数据集”这一整条路线的基准论文。PoseCNN 正好把这块历史底座补上。",
        "recommendation_en": "The library already had stronger later pose systems, but it still lacked the milestone paper that defined the known-object RGB pose pipeline and introduced YCB-Video.",
        "influence_cn": "影响力依据：OpenAlex 记录的被引数约 2099，Crossref 记录的 referenced-by 约 1486；发表在 RSS 2018，并伴随 YCB-Video 数据集一起成为 6D 位姿估计领域的常驻参照系。",
        "innovation_cn": "它最重要的机器人创新点，是把“抓取前的目标感知”从特征工程和模板匹配，推进到端到端可训练的 6D pose 网络，并且明确处理了遮挡、对称物体和真实台面杂乱场景这些机器人真正会遇到的问题。",
        "innovation_en": "Its robotics contribution is turning pre-grasp object pose estimation into a trainable end-to-end perception module that explicitly handles clutter, occlusion, and symmetry.",
        "limitation_cn": "它的设定仍然是已知物体实例，不解决 category-level 泛化，也不直接解决 novel object pose；同时主体输入还是 RGB，深度更多用于后处理 refinement，这也是后来 DenseFusion、NOCS、FoundationPose 继续往前推的地方。",
        "limitation_en": "It assumes known object instances, not category-level or open-world pose, and depth mainly enters as refinement rather than an integrated representation.",
        "core_cn": [
            "把 3D 平移拆成 2D 物体中心定位加距离回归，再用四元数回归旋转，降低直接回归完整 6D pose 的难度。",
            "提出面向对称物体的 ShapeMatch-Loss，减少姿态标签多解导致的训练不稳定。",
            "同步发布 YCB-Video 数据集，提供 21 个 YCB 物体、92 段视频和 133,827 帧精确位姿标注，成为后续大量 6D pose 论文的共同评测底座。",
        ],
        "core_en": [
            "Decouples translation into image-center localization plus depth prediction, and regresses rotation with quaternions.",
            "Introduces a symmetry-aware loss to stabilize training on objects with ambiguous orientations.",
            "Releases the YCB-Video dataset, which became a standard benchmark substrate for later 6D pose research.",
        ],
        "terms": [
            ("known-object pose estimation", "已知物体位姿估计"),
            ("ShapeMatch-Loss", "形状匹配损失"),
            ("YCB-Video", "YCB-Video 数据集"),
            ("occluded object pose", "遮挡场景位姿估计"),
        ],
        "repro": [
            "先把 PoseCNN 的问题设定和 NOCS、FoundationPose 区分清楚：它解决的是已知物体实例，不是类别泛化。",
            "重点复看平移与旋转分头预测的设计，以及对称物体损失怎么避开标签多解。",
            "顺手把 YCB-Video toolbox 一起看掉，因为后面很多 6D pose 论文的训练和评测接口都沿用了这条线。",
        ],
        "source_note": "来源组合：RSS 2018 论文 PDF、arXiv 页面、Washington 项目页、PoseCNN GitHub、YCB-Video toolbox、OpenAlex、Crossref。",
        "topic_tokens": "6d pose estimation object pose estimation rgb pose perception clutter known-object pose robotic manipulation",
        "search_tokens": "PoseCNN 6D object pose estimation cluttered scenes YCB-Video symmetric object occlusion RGB robotic manipulation",
        "topic_badges": ["6d pose estimation", "object pose estimation", "rgb pose", "perception"],
        "english_pills": ["6D pose", "RGB pose", "YCB-Video", "known object"],
    },
    {
        "title": "AnyGrasp: Robust and Efficient Grasp Perception in Spatial and Temporal Domains",
        "slug": "anygrasp",
        "pdf_url": "https://arxiv.org/pdf/2212.08333.pdf",
        "arxiv_url": "https://arxiv.org/abs/2212.08333",
        "landing_url": "https://graspnet.net/anygrasp.html",
        "doi_url": "https://doi.org/10.1109/TRO.2023.3281153",
        "project_url": "https://graspnet.net/anygrasp.html",
        "code_url": "https://github.com/graspnet/anygrasp_sdk",
        "extra_url": "https://graspnet.net/",
        "authors": "Hao-Shu Fang, Chenxi Wang, Hongjie Fang, Minghao Gou, Jirong Liu, Hengxu Yan, Wenhai Liu, Yichen Xie, Cewu Lu",
        "venue": "IEEE Transactions on Robotics (T-RO)",
        "year": "2023",
        "reading_status": "待复现",
        "desc_cn": "面向真实抓取系统落地的高性能抓取感知论文，强调 7-DoF、密集、连续、抗噪声和真实机器人吞吐，而不是只在静态单帧上报一个好看的抓取点。",
        "desc_en": "A high-throughput real-robot grasping paper focused on dense, stable, and temporally consistent grasp perception.",
        "brief_cn": "AnyGrasp 值得补进来，不是因为它“又是一个抓取模型”，而是因为它代表了 GraspNet 之后那条更工程化、更接近真实产线的路线：抓取感知不只是单次检测，而是要兼顾稳定性、速度、噪声鲁棒性和跨观测连续性。",
        "brief_en": "It matters because it pushes grasping from benchmark prediction toward a deployable real-robot perception stack with throughput and stability constraints.",
        "one_line_cn": "如果 GraspNet-1Billion 回答的是“怎样把抓取研究放到统一赛道”，那 AnyGrasp 回答的就是“在这条赛道上，什么样的系统才真的像一套能落地的抓取感知引擎”。",
        "recommendation_cn": "当前论文库里已经有 Dex-Net 2.0、Contact-GraspNet、GraspNet-1Billion 这些经典节点，但还缺一篇能把 benchmark 规模、真实部署速度、动态追踪和大批量未见物体抓取成功率串起来的系统论文。AnyGrasp 正好补上这段从 benchmark 走向真实系统的桥。",
        "recommendation_en": "The library already had grasp planning, grasp generation, and the GraspNet benchmark, but it still lacked the paper that best bridges those ideas into a high-throughput deployed grasping system.",
        "influence_cn": "影响力依据：OpenAlex 被引数约 210，Crossref referenced-by 约 227；发表在 T-RO 2023，并且项目页、SDK 和 GraspNet 生态一起推动了它在真实抓取系统里的扩散。",
        "innovation_cn": "它最值得机器人实践者重视的点，是把抓取感知从“单帧候选抓取生成”推进到“跨时序连续、考虑质心稳定性、兼顾噪声鲁棒和吞吐率”的系统能力，明显更接近真实 bin picking 和动态抓取部署要求。",
        "innovation_en": "Its key robotics value is reframing grasp perception as a temporally consistent, stability-aware, deployment-minded system rather than a one-shot detector.",
        "limitation_cn": "它虽然非常强，但主设定仍然围绕平行夹爪和特定抓取执行链路；对于多指灵巧手、任务语义约束抓取、复杂接触动力学，覆盖仍然有限。",
        "limitation_en": "It is still centered on parallel-jaw grasping and does not fully solve dexterous-hand, semantic, or contact-rich grasp execution.",
        "core_cn": [
            "在空间和时间两个维度上做密集监督，把真实感知与解析标注结合起来，提升抓取分布质量。",
            "显式引入物体质心相关信息，提升抓取稳定性而不只是可接近性。",
            "利用跨观测抓取对应关系做动态抓取追踪，在真实系统里兼顾 93.3% 未见物体 bin clearing 成功率和每小时 900+ picks 的吞吐表现。",
        ],
        "core_en": [
            "Uses dense supervision across both spatial and temporal domains, mixing real perception with analytic labels.",
            "Adds center-of-mass awareness to favor stable grasps rather than merely reachable ones.",
            "Tracks grasp correspondences across observations to support dynamic grasping with strong real-system throughput.",
        ],
        "terms": [
            ("grasp perception", "抓取感知"),
            ("temporal grasp tracking", "时序抓取跟踪"),
            ("center-of-mass awareness", "质心感知"),
            ("bin clearing throughput", "清箱吞吐率"),
        ],
        "repro": [
            "先把它和 Contact-GraspNet 对着读：前者更强调系统级稳定、时序和吞吐，后者更像高质量 6-DoF grasp generation 基座。",
            "重点看 dense supervision、质心约束和 grasp correspondence 这三块，它们解释了它为什么在真实系统里更稳。",
            "如果要复现，优先沿项目页和 SDK 跑通接口，再回看它与 GraspNet benchmark、动态抓取 demo 的衔接。",
        ],
        "source_note": "来源组合：T-RO DOI 页面、arXiv PDF、GraspNet AnyGrasp 项目页、AnyGrasp SDK、OpenAlex、Crossref。",
        "topic_tokens": "grasping grasp detection grasp tracking 7-dof grasp manipulation perception real-robot deployment foundation-model-assisted grasping ecosystem",
        "search_tokens": "AnyGrasp robust efficient grasp perception spatial temporal domains grasp tracking bin picking unseen objects T-RO real robot",
        "topic_badges": ["grasping", "grasp detection", "grasp tracking", "real deployment"],
        "english_pills": ["grasping", "real robot", "temporal", "throughput"],
    },
]


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def safe_title_for_filename(title: str) -> str:
    title = title.replace(":", " -")
    return re.sub(r'[<>:"/\\|?*]', "_", title)


def long_path(path: Path) -> str:
    resolved = str(path.resolve())
    if resolved.startswith("\\\\?\\") or len(resolved) < 240:
        return resolved
    return "\\\\?\\" + resolved


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def ul(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{html.escape(item)}</li>" for item in items) + "</ul>"


def terms_grid(items: list[tuple[str, str]]) -> str:
    return "".join(
        f'<div class="term"><span class="en">{html.escape(en)}</span><br />{html.escape(cn)}</div>'
        for en, cn in items
    )


def desktop_uri() -> str:
    return DESKTOP_ROOT.as_posix()


def download_pdf(paper: dict) -> None:
    file_name = f'{safe_title_for_filename(paper["title"])} - {TODAY}.pdf'
    desktop_path = DESKTOP_ROOT / file_name
    repo_path = WORKFLOW_ROOT / "papers" / file_name
    output_path = OUTPUTS_ROOT / "papers" / file_name
    if not desktop_path.exists():
        urllib.request.urlretrieve(paper["pdf_url"], long_path(desktop_path))
    for target in (repo_path, output_path):
        if not target.exists():
            shutil.copy2(long_path(desktop_path), long_path(target))
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
    <p class="subtitle">今日创新点：今天这组更像是在补“感知到抓取执行”中间最容易断掉的一段。PoseCNN 把已知物体在杂乱场景里的 6D 位姿估计做成了可训练、可比较的视觉前端；AnyGrasp 则把抓取感知进一步推成一套真正面向速度、稳定性和连续性的真实系统能力。</p>
    <p class="subtitle">未来创新点：下一步最值得追的是把这两条线接起来：前端用更强的位姿/几何理解稳住目标状态，中间用 foundation-model-assisted reasoning 做目标筛选和抓取约束，后端用 AnyGrasp 这一类高吞吐抓取感知系统完成真实落地。</p>
    <div class="meta">更新时间：{TODAY} · 今日论文：{TODAY} 追加刷新</div>
    <div class="top-actions"><a class="btn secondary" href="./robotics-paper-feishu-page-en.html">English Translation</a></div>
    <p class="local">论文库地址：<a href="./paper-folder-index.html">./paper-folder-index.html</a></p>

    <div class="callout">
      今日主题：用一篇经典 6D 位姿估计奠基论文，对照一篇更接近真实抓取部署的 T-RO 系统论文，补足当前论文库在“已知物体感知底座 / 抓取系统落地 / benchmark 之后怎么变成工程能力”上的结构空位。
    </div>

    <section class="today-grid" aria-label="今日重点总览">
      <div class="today-card"><strong>先读顺序</strong>先读 PoseCNN，把 YCB-Video、对称物体、遮挡鲁棒这条底线想清楚；再读 AnyGrasp，看 benchmark 之后怎样把抓取真正做成高吞吐系统。</div>
      <div class="today-card"><strong>关键词</strong>6D pose estimation、YCB-Video、RGB pose、grasp perception、temporal grasp tracking、bin picking。</div>
      <div class="today-card"><strong>今日追问</strong>如果以后要做 foundation-model-assisted grasping，真正短板更可能出在位姿前端、抓取分布建模，还是系统时序稳定性？</div>
      <div class="today-card"><strong>影响力依据</strong>PoseCNN 在 OpenAlex 上约 2099 次引用，AnyGrasp 约 210 次；前者是经典底座，后者是近年的高质量系统代表。</div>
      <div class="today-card"><strong>互补性</strong>前者解决“目标怎么看准”，后者解决“看准之后怎样又稳又快地持续抓”。</div>
    </section>

    <h2 id="{p1["slug"]}">论文 1</h2>
    <p class="paper-title en">{html.escape(p1["title"])}（{TODAY}）</p>
    <p>论文链接：<a href="{p1["arxiv_url"]}">{p1["arxiv_url"]}</a> · DOI：<a href="{p1["doi_url"]}">{p1["doi_url"].replace("https://doi.org/", "")}</a></p>
    <div class="actions">
      <a class="btn" href="./papers/{html.escape(p1["file_name"])}">打开 PDF</a>
      <a class="btn secondary" href="./paper-folder-index.html">论文库</a>
      <a class="btn secondary" href="./translations/{p1["slug"]}.html">论文翻译</a>
      <a class="btn secondary" href="{p1["arxiv_url"]}">arXiv</a>
    </div>
    <p><span class="tag">6D 位姿估计</span><span class="tag">YCB-Video</span><span class="tag">遮挡鲁棒</span><span class="tag">RGB 感知</span></p>
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
    <p>论文链接：<a href="{p2["arxiv_url"]}">{p2["arxiv_url"]}</a> · DOI：<a href="{p2["doi_url"]}">{p2["doi_url"].replace("https://doi.org/", "")}</a></p>
    <div class="actions">
      <a class="btn" href="./papers/{html.escape(p2["file_name"])}">打开 PDF</a>
      <a class="btn secondary" href="./paper-folder-index.html">论文库</a>
      <a class="btn secondary" href="./translations/{p2["slug"]}.html">论文翻译</a>
      <a class="btn secondary" href="{p2["arxiv_url"]}">arXiv</a>
    </div>
    <p><span class="tag">抓取感知</span><span class="tag">时序连续性</span><span class="tag">真实部署</span><span class="tag">高吞吐</span></p>
    <h3>两篇论文介绍</h3>
    <p>{html.escape(p2["desc_cn"])}</p>
    <h3>核心方法</h3>
    {ul(p2["core_cn"])}
    <h3>我认为的机器人创新点</h3>
    <p>{html.escape(p2["innovation_cn"])}</p>
    <h3>局限</h3>
    <p>{html.escape(p2["limitation_cn"])}</p>

    <h2>对比结论</h2>
    <p><strong>PoseCNN</strong> 更偏“把感知底座做稳”，尤其是已知物体、RGB 输入、遮挡和对称物体这些抓取前最容易掉链子的环节。</p>
    <p><strong>AnyGrasp</strong> 更偏“把抓取系统做成真实能力”，强调连续、稳定、抗噪和吞吐，而不是只在静态评测里给一个候选抓取。</p>
    <p>这两篇连着读，能把论文库里“6D pose / benchmark / 6-DoF grasp generation”之间缺掉的那一段桥补上。</p>

    <h3>阅读顺序</h3>
    <p>先读 <span class="en">PoseCNN</span>，再读 <span class="en">AnyGrasp</span>。</p>
  </main>
</body>
</html>
"""


def english_main_page(p1: dict, p2: dict) -> str:
    desk = desktop_uri()
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
    <p class="subtitle">Today's innovation point: this pair repairs a missing bridge in the current library. PoseCNN establishes a durable known-object 6D pose front-end for cluttered manipulation scenes, while AnyGrasp shows what it takes to turn grasp perception into a fast, stable, real-robot system.</p>
    <p class="subtitle">Next innovation point: combine stronger pose understanding with foundation-assisted target reasoning, then hand off to deployment-grade grasp perception for robust closed-loop manipulation.</p>
    <div class="meta">Updated: {TODAY} · appended daily refresh</div>
    <div class="top-actions"><a class="btn secondary" href="robotics-paper-feishu-page.html">返回中文</a></div>
    <p class="local">Paper library: <a href="file:///{desk}/index.html">file:///{desk}/index.html</a></p>
    <div class="callout">Today's pair is intentionally complementary: PoseCNN stabilizes the pre-grasp pose front-end under clutter and symmetry, while AnyGrasp pushes grasp perception toward deployment-grade continuity, throughput, and stability.</div>
    <section class="today-grid">
      <div class="today-card"><strong>Read First</strong>Read PoseCNN first, then AnyGrasp.</div>
      <div class="today-card"><strong>Keywords</strong>6D pose, YCB-Video, RGB pose, grasp perception, temporal tracking, bin picking.</div>
      <div class="today-card"><strong>Impact</strong>OpenAlex counts are about 2099 for PoseCNN and 210 for AnyGrasp.</div>
      <div class="today-card"><strong>Complement</strong>Perception foundation versus real-system grasp execution readiness.</div>
    </section>
    <h2 id="{p1["slug"]}">Paper 1</h2>
    <p class="paper-title">{html.escape(p1["title"])} ({TODAY})</p>
    <p>Links: <a href="{p1["arxiv_url"]}">arXiv</a> · DOI: <a href="{p1["doi_url"]}">{p1["doi_url"].replace("https://doi.org/", "")}</a></p>
    <div class="actions">
      <a class="btn" href="file:///{desk}/{html.escape(p1["file_name"])}">Open PDF</a>
      <a class="btn secondary" href="file:///{desk}/index.html">Paper Library</a>
      <a class="btn secondary" href="file:///{desk}/translations/{p1["slug"]}.html">View Analysis</a>
      <a class="btn secondary" href="{p1["arxiv_url"]}">arXiv</a>
    </div>
    <p><span class="tag">6D pose</span><span class="tag">RGB</span><span class="tag">YCB-Video</span><span class="tag">clutter</span></p>
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
    <p>Links: <a href="{p2["arxiv_url"]}">arXiv</a> · DOI: <a href="{p2["doi_url"]}">{p2["doi_url"].replace("https://doi.org/", "")}</a></p>
    <div class="actions">
      <a class="btn" href="file:///{desk}/{html.escape(p2["file_name"])}">Open PDF</a>
      <a class="btn secondary" href="file:///{desk}/index.html">Paper Library</a>
      <a class="btn secondary" href="file:///{desk}/translations/{p2["slug"]}.html">View Analysis</a>
      <a class="btn secondary" href="{p2["arxiv_url"]}">arXiv</a>
    </div>
    <p><span class="tag">grasping</span><span class="tag">temporal</span><span class="tag">real robot</span><span class="tag">throughput</span></p>
    <h3>Why It Was Chosen</h3>
    <p>{html.escape(p2["recommendation_en"])}</p>
    <h3>Core Methods</h3>
    {ul(p2["core_en"])}
    <h3>Robotics Insight</h3>
    <p>{html.escape(p2["innovation_en"])}</p>
    <h3>Main Limitation</h3>
    <p>{html.escape(p2["limitation_en"])}</p>

    <h2>Comparison</h2>
    <p><strong>PoseCNN</strong> is about making known-object pose estimation in clutter trainable, standard, and useful to downstream manipulation.</p>
    <p><strong>AnyGrasp</strong> is about making grasp perception continuous, stable, and fast enough for real deployment rather than isolated evaluation.</p>
    <p>Read them in that order to connect perception infrastructure with deployment-minded grasp execution.</p>
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
    <p class="note">建议把它和今天另一篇论文对照着读，重点看它补的是机器人感知链路、抓取链路还是系统链路的哪一层。</p>
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
    <p><strong>DOI：</strong><a href="{paper["doi_url"]}">{paper["doi_url"].replace("https://doi.org/", "")}</a></p>
    <p><strong>arXiv：</strong><a href="{paper["arxiv_url"]}">{paper["arxiv_url"].replace("https://arxiv.org/abs/", "")}</a></p>
    <p><strong>项目 / 代码：</strong><a href="{paper["project_url"]}">{paper["project_url"]}</a> · <a href="{paper["code_url"]}">{paper["code_url"]}</a></p>
    <p><strong>补充资源：</strong><a href="{paper["extra_url"]}">{paper["extra_url"]}</a></p>
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
        <div class="meta"><label class="status-control">状态：<select class="status-editor" aria-label="修改 {paper["slug"]} 阅读状态">{"".join(options)}</select></label>{pills}<span class="pill">{paper["file_size_mb"]} MB</span></div>
        <div class="actions"><a class="btn" href="{html.escape(paper["file_name"])}">打开 PDF</a><a class="btn secondary" href="{analysis_href}">查看分析结果</a><a class="btn secondary" href="{paper["arxiv_url"]}">arXiv</a></div>
      </article>
"""


def english_article_block(paper: dict, index_number: int, analysis_href: str, pdf_href: str) -> str:
    first_pill = html.escape(paper["english_pills"][0])
    second_pill = html.escape(paper["english_pills"][1])
    return (
        f'<article class="paper"><span class="badge">Paper {index_number} · {TODAY}</span>'
        f'<h2 class="title">{html.escape(paper["title"])}</h2>'
        f'<p class="desc">{html.escape(paper["desc_en"])}</p>'
        f'<div class="brief"><strong>Summary:</strong> {html.escape(paper["brief_en"])}</div>'
        f'<div class="meta"><span class="pill">{paper["file_size_mb"]} MB</span><span class="pill">{first_pill}</span><span class="pill">{second_pill}</span></div>'
        f'<div class="actions"><a class="btn" href="{pdf_href}">Open PDF</a><a class="btn secondary" href="{analysis_href}">View Analysis</a><a class="btn secondary" href="{paper["arxiv_url"]}">arXiv</a></div></article>'
    )


def append_unique_article(content: str, article_html: str, title: str) -> str:
    if title in content:
        return content
    return re.sub(
        r'(?s)(<section class="grid" id="paperGrid">)(.*?)(</section>)',
        lambda m: m.group(1) + m.group(2) + article_html + "\n    " + m.group(3),
        content,
        count=1,
    )


def append_unique_english_article(content: str, article_html: str, title: str) -> str:
    if title in content:
        return content
    return re.sub(
        r'(?s)(<section class="grid">)(.*?)(</section>)',
        lambda m: m.group(1) + m.group(2) + article_html + m.group(3),
        content,
        count=1,
    )


def update_chinese_library(path: Path, analysis_mode: str) -> int:
    content = read_text(path)
    current_count = len(re.findall(r'<article class="paper"', content))
    for paper in PAPERS:
        if paper["title"] in content:
            continue
        current_count += 1
        analysis_href = f"translations/{paper['slug']}.html" if analysis_mode == "outputs" else f"../index.html#{paper['slug']}"
        content = append_unique_article(content, chinese_article_block(paper, current_count, analysis_href), paper["title"])

    content = re.sub(
        r'(?s)<section class="panel">.*?</section>\s*<section class="grid" id="paperGrid">',
        """
    <section class="panel">
      <h2>今日重点</h2>
      <div class="overview">
        <div class="overview-card"><strong>先读建议：</strong>先读 PoseCNN，把“已知物体在杂乱场景里怎样稳定位姿”这条线补齐；再读 AnyGrasp，看抓取感知怎样从 benchmark 走到真实高吞吐系统。</div>
        <div class="overview-card"><strong>研究抓手：</strong>今天补的是“位姿底座 + 系统级抓取感知”这一段。它能把论文库里已有的 NOCS、DenseFusion、Contact-GraspNet、GraspNet-1Billion 串成一条更完整的感知到执行链。</div>
      </div>
      <div class="controls" aria-label="搜索与筛选">
        <input id="searchBox" type="search" placeholder="搜索标题、标签、方向，例如 pose / YCB / grasp / temporal / clutter / bin picking" />
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
          <option value="rgb pose">rgb pose</option>
          <option value="foundation-model-assisted pose">foundation-model-assisted pose</option>
          <option value="grasping">grasping</option>
          <option value="grasp planning">grasp planning</option>
          <option value="grasp detection">grasp detection</option>
          <option value="grasp tracking">grasp tracking</option>
          <option value="real deployment">real deployment</option>
        </select>
        <select id="pageSize">
          <option value="2">每页 2 篇</option>
          <option value="4">每页 4 篇</option>
          <option value="8">每页 8 篇</option>
        </select>
      </div>
    </section>

    <section class="grid" id="paperGrid">""",
        content,
        count=1,
    )
    total = len(re.findall(r'<article class="paper"', content))
    content = re.sub(r"当前日期：\d{4}-\d{2}-\d{2} · 累计收录 \d+ 篇", f"当前日期：{TODAY} · 累计收录 {total} 篇", content)
    content = re.sub(
        r"libraryCount\.textContent = `当前日期：\d{4}-\d{2}-\d{2} · 累计收录 \$\{papers\.length\} 篇`;",
        f"libraryCount.textContent = `当前日期：{TODAY} · 累计收录 ${{papers.length}} 篇`;",
        content,
    )
    content = re.sub(r"当前日期：\d{4}-\d{2}-\d{2} · 累计收录 \${papers.length} 篇", f"当前日期：{TODAY} · 累计收录 ${{papers.length}} 篇", content)
    write_text(path, content)
    return total


def update_english_library(path: Path, outputs_mode: bool) -> int:
    content = read_text(path)
    current_count = len(re.findall(r'<article class="paper">', content))
    for paper in PAPERS:
        if paper["title"] in content:
            continue
        current_count += 1
        analysis_href = (
            f"file:///{desktop_uri()}/translations/{paper['slug']}.html"
            if outputs_mode
            else f"../index-en.html#{paper['slug']}"
        )
        pdf_href = paper["file_name"]
        content = append_unique_english_article(content, english_article_block(paper, current_count, analysis_href, pdf_href), paper["title"])

    total = len(re.findall(r'<article class="paper">', content))
    folder_href = f"file:///{desktop_uri()}/" if outputs_mode else "./"
    content = re.sub(
        r'<div class="toolbar"><span>Date: .*?</span><a class="open-folder" href=".*?">Open folder</a></div>',
        f'<div class="toolbar"><span>Date: {TODAY} · {total} papers</span><a class="open-folder" href="{folder_href}">Open folder</a></div>',
        content,
    )
    filters = '<section class="filters"><span class="filter">manipulation</span><span class="filter">benchmark</span><span class="filter">VLA</span><span class="filter">SLAM</span><span class="filter">perception</span><span class="filter">6D pose</span><span class="filter">RGB pose</span><span class="filter">grasping</span><span class="filter">grasp tracking</span><span class="filter">real deployment</span></section>'
    content = re.sub(r'(?s)<section class="filters">.*?</section>', filters, content, count=1)
    write_text(path, content)
    return total


def update_launcher(path: Path) -> None:
    content = read_text(path)
    replacements = {
        r'\$dexTranslationPath = Join-Path \$libraryRoot "translations\\.*?\.html"': '$firstAnalysisPath = Join-Path $libraryRoot "translations\\posecnn.html"',
        r'\$roboTranslationPath = Join-Path \$libraryRoot "translations\\.*?\.html"': '$secondAnalysisPath = Join-Path $libraryRoot "translations\\anygrasp.html"',
        r'Open .*? translation': 'Open PoseCNN analysis',
        r'Open .*? translation': 'Open AnyGrasp analysis',
    }
    content = re.sub(
        r'\$dexTranslationPath = Join-Path \$libraryRoot "translations\\.*?\.html"',
        lambda _: '$firstAnalysisPath = Join-Path $libraryRoot "translations\\posecnn.html"',
        content,
    )
    content = re.sub(
        r'\$roboTranslationPath = Join-Path \$libraryRoot "translations\\.*?\.html"',
        lambda _: '$secondAnalysisPath = Join-Path $libraryRoot "translations\\anygrasp.html"',
        content,
    )
    content = content.replace("Open DexSim2Real translation", "Open PoseCNN analysis")
    content = content.replace("Open RoboWM-Bench translation", "Open AnyGrasp analysis")
    content = content.replace("Open NOCS analysis", "Open PoseCNN analysis")
    content = content.replace("Open GraspNet-1Billion analysis", "Open AnyGrasp analysis")
    content = content.replace(
        '$openDexTranslation.Add_Click({ if (Test-Path $dexTranslationPath) { Start-Process -FilePath $dexTranslationPath } })',
        '$openDexTranslation.Add_Click({ if (Test-Path $firstAnalysisPath) { Start-Process -FilePath $firstAnalysisPath } })',
    )
    content = content.replace(
        '$openRoboTranslation.Add_Click({ if (Test-Path $roboTranslationPath) { Start-Process -FilePath $roboTranslationPath } })',
        '$openRoboTranslation.Add_Click({ if (Test-Path $secondAnalysisPath) { Start-Process -FilePath $secondAnalysisPath } })',
    )
    write_text(path, content)


def sync_to_desktop() -> None:
    shutil.copy2(OUTPUTS_ROOT / "paper-folder-index.html", DESKTOP_ROOT / "index.html")
    shutil.copy2(OUTPUTS_ROOT / "paper-folder-index-en.html", DESKTOP_ROOT / "index-en.html")
    shutil.copytree(OUTPUTS_ROOT / "translations", DESKTOP_ROOT / "translations", dirs_exist_ok=True)


def main() -> None:
    ensure_dir(DESKTOP_ROOT)
    ensure_dir(DESKTOP_ROOT / "translations")
    ensure_dir(OUTPUTS_ROOT / "papers")
    ensure_dir(OUTPUTS_ROOT / "translations")
    ensure_dir(WORKFLOW_ROOT / "papers")
    ensure_dir(WORKFLOW_ROOT / "papers" / "translations")

    for paper in PAPERS:
        download_pdf(paper)

    cn_main = chinese_main_page(PAPERS[0], PAPERS[1])
    en_main = english_main_page(PAPERS[0], PAPERS[1])
    write_text(OUTPUTS_ROOT / "robotics-paper-feishu-page.html", cn_main)
    write_text(WORKFLOW_ROOT / "index.html", cn_main)
    write_text(OUTPUTS_ROOT / "robotics-paper-feishu-page-en.html", en_main)
    write_text(WORKFLOW_ROOT / "index-en.html", en_main)

    for paper in PAPERS:
        write_text(
            OUTPUTS_ROOT / "translations" / f"{paper['slug']}.html",
            translation_page(paper, "../paper-folder-index.html", f"../papers/{paper['file_name']}"),
        )
        write_text(
            WORKFLOW_ROOT / "papers" / "translations" / f"{paper['slug']}.html",
            translation_page(paper, "../index.html", f"../{paper['file_name']}"),
        )

    update_chinese_library(OUTPUTS_ROOT / "paper-folder-index.html", "outputs")
    update_chinese_library(WORKFLOW_ROOT / "papers" / "index.html", "repo")
    update_english_library(OUTPUTS_ROOT / "paper-folder-index-en.html", True)
    update_english_library(WORKFLOW_ROOT / "papers" / "index-en.html", False)

    sync_to_desktop()

    update_launcher(ROOT / "work" / "robot-paper-dynamic-launcher.ps1")
    update_launcher(WORKFLOW_ROOT / "scripts" / "robot-paper-dynamic-launcher.ps1")


if __name__ == "__main__":
    main()
