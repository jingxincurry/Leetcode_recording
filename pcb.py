from pathlib import Path

svg = r'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1400" height="1000" viewBox="0 0 1400 1000" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .bg{fill:#fbfbfb}
      .title{font-family:"Microsoft YaHei","Noto Sans CJK SC",Arial,sans-serif;font-size:38px;font-weight:700;fill:#111}
      .subtitle{font-family:"Microsoft YaHei","Noto Sans CJK SC",Arial,sans-serif;font-size:18px;fill:#333}
      .h1{font-family:"Microsoft YaHei","Noto Sans CJK SC",Arial,sans-serif;font-size:22px;font-weight:700;fill:#111}
      .h2{font-family:"Microsoft YaHei","Noto Sans CJK SC",Arial,sans-serif;font-size:18px;font-weight:700;fill:#111}
      .txt{font-family:"Microsoft YaHei","Noto Sans CJK SC",Arial,sans-serif;font-size:16px;fill:#222}
      .small{font-family:"Microsoft YaHei","Noto Sans CJK SC",Arial,sans-serif;font-size:14px;fill:#333}
      .note{font-family:"Microsoft YaHei","Noto Sans CJK SC",Arial,sans-serif;font-size:15px;fill:#444}
      .box{fill:#fff;stroke:#333;stroke-width:1.6;rx:12}
      .green{fill:#eef9e9;stroke:#4f8a3d;stroke-width:1.8;rx:12}
      .yellow{fill:#fff7df;stroke:#e09b22;stroke-width:1.8;rx:12}
      .purple{fill:#f4edff;stroke:#7e57c2;stroke-width:1.8;rx:12}
      .red{fill:#fff0f0;stroke:#d9534f;stroke-width:1.8;rx:12}
      .blue{fill:#eef6ff;stroke:#2f80ed;stroke-width:1.8;rx:12}
      .orange{fill:#fff4e6;stroke:#f2994a;stroke-width:1.8;rx:12}
      .cyan{fill:#ecfbfb;stroke:#21a3a3;stroke-width:1.8;rx:12}
      .cell{fill:#fff;stroke:#999;stroke-width:1}
      .line{stroke:#333;stroke-width:1.8;fill:none}
      .thin{stroke:#777;stroke-width:1.2;fill:none}
      .arrow{stroke:#333;stroke-width:2;fill:none;marker-end:url(#arrow)}
      .darrow{stroke:#555;stroke-width:1.8;fill:none;stroke-dasharray:7 6;marker-end:url(#arrow)}
    </style>
    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
      <path d="M2,2 L10,6 L2,10 Z" fill="#333"/>
    </marker>
  </defs>

  <rect class="bg" x="0" y="0" width="1400" height="1000"/>
  <text x="700" y="50" text-anchor="middle" class="title">PCB（进程控制块）结构图</text>
  <text x="700" y="82" text-anchor="middle" class="subtitle">PCB 是操作系统内核用于表示、管理和切换进程的核心数据结构（Linux 中主要对应 task_struct）</text>

  <text x="55" y="520" class="title" fill="#174ea6">PCB</text>
  <path d="M105 120 C75 120,75 120,75 155 L75 850 C75 885,75 885,105 885" fill="none" stroke="#174ea6" stroke-width="3"/>

  <rect x="120" y="120" width="500" height="120" class="green"/>
  <text x="370" y="152" text-anchor="middle" class="h1">1. 进程标识信息</text>
  <rect x="145" y="175" width="80" height="34" class="cell"/><text x="185" y="198" text-anchor="middle" class="txt">PID</text>
  <rect x="240" y="175" width="80" height="34" class="cell"/><text x="280" y="198" text-anchor="middle" class="txt">PPID</text>
  <rect x="335" y="175" width="80" height="34" class="cell"/><text x="375" y="198" text-anchor="middle" class="txt">TGID</text>
  <rect x="430" y="175" width="80" height="34" class="cell"/><text x="470" y="198" text-anchor="middle" class="txt">UID/GID</text>
  <text x="370" y="228" text-anchor="middle" class="small">用于唯一识别进程、父进程、线程组和用户权限</text>

  <rect x="120" y="250" width="500" height="120" class="yellow"/>
  <text x="370" y="282" text-anchor="middle" class="h1">2. 进程状态与调度信息</text>
  <rect x="145" y="305" width="450" height="28" class="cell"/><text x="370" y="325" text-anchor="middle" class="txt">状态：运行 / 就绪 / 阻塞 / 僵尸 / 停止</text>
  <rect x="145" y="333" width="450" height="28" class="cell"/><text x="370" y="353" text-anchor="middle" class="txt">优先级 priority、调度策略 policy、时间片</text>

  <rect x="120" y="380" width="500" height="160" class="purple"/>
  <text x="370" y="412" text-anchor="middle" class="h1">3. CPU 上下文信息（寄存器现场）</text>
  <rect x="145" y="435" width="220" height="28" class="cell"/><text x="255" y="455" text-anchor="middle" class="txt">PC / RIP（程序计数器）</text>
  <rect x="375" y="435" width="220" height="28" class="cell"/><text x="485" y="455" text-anchor="middle" class="txt">SP / RSP（栈指针）</text>
  <rect x="145" y="463" width="90" height="28" class="cell"/><text x="190" y="483" text-anchor="middle" class="txt">RAX</text>
  <rect x="235" y="463" width="90" height="28" class="cell"/><text x="280" y="483" text-anchor="middle" class="txt">RBX</text>
  <rect x="325" y="463" width="90" height="28" class="cell"/><text x="370" y="483" text-anchor="middle" class="txt">RCX</text>
  <rect x="415" y="463" width="90" height="28" class="cell"/><text x="460" y="483" text-anchor="middle" class="txt">RDX</text>
  <rect x="505" y="463" width="90" height="28" class="cell"/><text x="550" y="483" text-anchor="middle" class="txt">...</text>
  <rect x="145" y="491" width="450" height="28" class="cell"/><text x="370" y="511" text-anchor="middle" class="txt">RFLAGS / EFLAGS、控制寄存器信息等</text>

  <rect x="120" y="550" width="500" height="125" class="red"/>
  <text x="370" y="582" text-anchor="middle" class="h1">4. 内存管理信息</text>
  <rect x="145" y="605" width="450" height="28" class="cell"/><text x="370" y="625" text-anchor="middle" class="txt">mm_struct 指针（进程地址空间）</text>
  <rect x="145" y="633" width="450" height="28" class="cell"/><text x="370" y="653" text-anchor="middle" class="txt">页表基址 CR3、虚拟内存区域链表 VMA</text>

  <rect x="120" y="685" width="500" height="120" class="blue"/>
  <text x="370" y="717" text-anchor="middle" class="h1">5. I/O 与文件信息</text>
  <rect x="145" y="740" width="450" height="28" class="cell"/><text x="370" y="760" text-anchor="middle" class="txt">打开文件描述符表 files_struct *</text>
  <rect x="145" y="768" width="450" height="28" class="cell"/><text x="370" y="788" text-anchor="middle" class="txt">当前工作目录、设备 I/O、网络连接</text>

  <rect x="120" y="815" width="500" height="90" class="cyan"/>
  <text x="370" y="847" text-anchor="middle" class="h1">6. 信号、资源限制与其他内核管理信息</text>
  <text x="150" y="880" class="txt">信号屏蔽字、rlimit、审计信息、安全能力 capability、创建/退出时间等</text>

  <rect x="710" y="120" width="560" height="120" class="blue" stroke-dasharray="8 6"/>
  <text x="990" y="152" text-anchor="middle" class="h1" fill="#174ea6">PCB 的作用</text>
  <text x="745" y="185" class="txt">1. 记录进程的各种管理信息</text>
  <text x="745" y="212" class="txt">2. 在上下文切换时保存 / 恢复进程现场</text>
  <text x="745" y="239" class="txt">3. 供调度器进行调度、管理和控制进程</text>

  <rect x="700" y="270" width="600" height="230" class="green"/>
  <text x="1000" y="305" text-anchor="middle" class="h1">CPU 上下文信息（详细）</text>
  <rect x="735" y="330" width="105" height="70" class="green"/>
  <text x="787" y="360" text-anchor="middle" class="txt">用户态</text>
  <text x="787" y="384" text-anchor="middle" class="txt">寄存器</text>
  <rect x="735" y="415" width="105" height="55" class="green"/>
  <text x="787" y="438" text-anchor="middle" class="txt">内核态</text>
  <text x="787" y="460" text-anchor="middle" class="txt">寄存器</text>

  <rect x="860" y="325" width="390" height="80" class="cell"/>
  <line x1="990" y1="325" x2="990" y2="405" class="thin"/>
  <line x1="1120" y1="325" x2="1120" y2="405" class="thin"/>
  <line x1="860" y1="352" x2="1250" y2="352" class="thin"/>
  <line x1="860" y1="378" x2="1250" y2="378" class="thin"/>
  <text x="925" y="345" text-anchor="middle" class="small">RIP</text>
  <text x="1055" y="345" text-anchor="middle" class="small">RSP</text>
  <text x="1185" y="345" text-anchor="middle" class="small">RFLAGS</text>
  <text x="925" y="371" text-anchor="middle" class="small">RAX / RBX</text>
  <text x="1055" y="371" text-anchor="middle" class="small">RCX / RDX</text>
  <text x="1185" y="371" text-anchor="middle" class="small">R8 ~ R15</text>
  <text x="1055" y="397" text-anchor="middle" class="small">保存进程在 CPU 上的执行现场</text>

  <rect x="860" y="420" width="390" height="55" class="cell"/>
  <line x1="990" y1="420" x2="990" y2="475" class="thin"/>
  <line x1="1120" y1="420" x2="1120" y2="475" class="thin"/>
  <text x="925" y="452" text-anchor="middle" class="small">CR3</text>
  <text x="1055" y="452" text-anchor="middle" class="small">FS / GS</text>
  <text x="1185" y="452" text-anchor="middle" class="small">内核栈指针</text>

  <path d="M620 455 C650 455,670 385,700 385" class="darrow"/>

  <rect x="700" y="525" width="600" height="245" class="orange"/>
  <text x="1000" y="558" text-anchor="middle" class="h1">进程地址空间信息（mm_struct）</text>
  <text x="745" y="600" class="small">高地址</text>
  <line x1="770" y1="615" x2="770" y2="720" class="line"/>
  <path d="M770 615 L762 628 M770 615 L778 628" class="line"/>
  <text x="745" y="742" class="small">低地址</text>

  <rect x="820" y="590" width="215" height="140" class="box"/>
  <rect x="820" y="590" width="215" height="28" fill="#eef9e9" stroke="#999"/>
  <text x="927" y="610" text-anchor="middle" class="small">内核空间（共享）</text>
  <rect x="820" y="618" width="215" height="28" fill="#fff" stroke="#999"/>
  <text x="927" y="638" text-anchor="middle" class="small">栈 Stack</text>
  <rect x="820" y="646" width="215" height="28" fill="#fff" stroke="#999"/>
  <text x="927" y="666" text-anchor="middle" class="small">堆 Heap</text>
  <rect x="820" y="674" width="215" height="28" fill="#fff" stroke="#999"/>
  <text x="927" y="694" text-anchor="middle" class="small">数据段 Data</text>
  <rect x="820" y="702" width="215" height="28" fill="#fff" stroke="#999"/>
  <text x="927" y="722" text-anchor="middle" class="small">代码段 Text/Code</text>

  <text x="1095" y="596" class="h2">VMA 链表</text>
  <rect x="1110" y="620" width="110" height="34" class="cell"/><text x="1165" y="642" text-anchor="middle" class="small">VMA 1</text>
  <rect x="1110" y="654" width="110" height="34" class="cell"/><text x="1165" y="676" text-anchor="middle" class="small">VMA 2</text>
  <rect x="1110" y="688" width="110" height="34" class="cell"/><text x="1165" y="710" text-anchor="middle" class="small">VMA 3</text>
  <path d="M1035 632 L1110 637" class="arrow"/>
  <path d="M1035 665 L1110 671" class="arrow"/>
  <path d="M1035 700 L1110 705" class="arrow"/>

  <path d="M620 612 C650 612,670 647,700 647" class="darrow"/>

  <rect x="700" y="795" width="600" height="140" class="purple"/>
  <text x="1000" y="828" text-anchor="middle" class="h1">上下文切换时 PCB 如何变化</text>
  <rect x="735" y="855" width="150" height="40" class="cell"/><text x="810" y="880" text-anchor="middle" class="small">保存当前进程现场</text>
  <rect x="920" y="855" width="150" height="40" class="cell"/><text x="995" y="880" text-anchor="middle" class="small">选择下一个进程</text>
  <rect x="1105" y="855" width="150" height="40" class="cell"/><text x="1180" y="880" text-anchor="middle" class="small">恢复新进程现场</text>
  <path d="M885 875 L920 875" class="arrow"/>
  <path d="M1070 875 L1105 875" class="arrow"/>
  <text x="735" y="920" class="small">本质：CPU 寄存器 ⇄ PCB 中保存的寄存器现场；CR3 切到新进程页表</text>

  <rect x="120" y="930" width="1180" height="42" class="box" stroke-dasharray="8 6"/>
  <text x="710" y="957" text-anchor="middle" class="note">PCB 由操作系统内核维护，用户进程不能直接访问；它是进程调度、资源管理和上下文切换的核心依据。</text>
</svg>
'''

path = Path('pcb_structure_diagram.svg')
path.write_text(svg, encoding='utf-8')
print(path.as_posix())
