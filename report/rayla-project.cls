%-----------------------------------------------------------------------------
% Author: Rayla Kurosaki
% GitHub: https://github.com/rkp1503
%-----------------------------------------------------------------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{rayla-project}[Rayla's Project's Class]
\LoadClass{article}

%-----------------------------------------------------------------------------
% Defining new commands
%-----------------------------------------------------------------------------
\newcommand{\myUniversity}[1]{\newcommand{\myUniversityLoc}{#1}}
\newcommand{\myTitle}[1]{\newcommand{\myTitleLoc}{#1}}
\newcommand{\myName}[1]{\newcommand{\myNameLoc}{#1}}
\newcommand{\courseid}[1]{\newcommand{\courseidLoc}{#1}}
\newcommand{\courseName}[1]{\newcommand{\courseNameLoc}{#1}}
\newcommand{\professorName}[1]{\newcommand{\professorNameLoc}{#1}}
\newcommand{\term}[1]{\newcommand{\termLoc}{#1}}
\newcommand{\dueDate}[1]{\newcommand{\dueDateLoc}{#1}}

%-----------------------------------------------------------------------------
% Document margins
%-----------------------------------------------------------------------------
\usepackage{geometry}
\geometry{left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm}
\setlength\parindent{0pt}
    
%-----------------------------------------------------------------------------
% Custom Title Style
%-----------------------------------------------------------------------------
\renewcommand{\maketitle}{
    \thispagestyle{plain}
    \begin{center}
        {\scshape \myUniversityLoc} \\[10pt]
        \hrule
        \vspace{10pt}
        {\LARGE \bfseries \myTitleLoc} \\[5pt]
        Student: {\itshape \myNameLoc}
        \vspace{8pt}
        \hrule
        \vspace{10pt}
        {Course: {\itshape \courseNameLoc \ (\courseidLoc)}} \hfill {Term: {\itshape \termLoc}}\\
        {Professor: {\itshape\professorNameLoc}} \hfill {Due date: {\itshape\dueDateLoc}}
        \vspace{20pt}
    \end{center}
}

%-----------------------------------------------------------------------------
% bibliography settings
%-----------------------------------------------------------------------------
\usepackage[backend=biber,style=numeric,sorting=ynt]{biblatex}
\addbibresource{main.bib}

%-----------------------------------------------------------------------------
% Dummy text
%-----------------------------------------------------------------------------
\usepackage{lipsum}
