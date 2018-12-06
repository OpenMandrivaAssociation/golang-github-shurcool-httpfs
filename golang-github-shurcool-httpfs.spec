# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/httpfs
%global commit          809beceb23714880abc4a382a00c05f89d13b1cc

%global common_description %{expand:
Collection of Go packages for working with the http.FileSystem interface.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Collection of Go packages for working with the http.FileSystem interface
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/shurcooL/httpgzip)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git809bece
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418git809bece
- First package for Fedora

