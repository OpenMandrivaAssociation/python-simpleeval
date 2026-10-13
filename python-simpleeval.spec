Name:		python-simpleeval
Version:	1.0.8
Release:	2
Summary:	Simple, safe single-expression evaluator
License:	MIT
Group:		Development/Python
URL:		https://github.com/danthedeckie/simpleeval
Source0:	https://files.pythonhosted.org/packages/source/s/simpleeval/simpleeval-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)

%description
A small library for safely evaluating simple Python expressions
without exposing builtins or imports. Used by ComfyUI for widget
expressions.

%files
%doc README.rst
%license LICENCE
%{py_sitedir}/simpleeval.py
%{py_sitedir}/__pycache__/simpleeval*.pyc
%{py_sitedir}/simpleeval-*.*-info
