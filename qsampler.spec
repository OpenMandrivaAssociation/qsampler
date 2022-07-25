Name:		qsampler
Summary:	LinuxSampler GUI front-end application
Version:	0.9.6
Release:	1
License:	GPLv2
Group:		Sound/Midi
URL:		https://qsampler.sourceforge.io/
Source0:	https://sourceforge.net/projects/qsampler/files/qsampler/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(lscp)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(gig)
BuildRequires:	cmake
BuildRequires:	qt5-qttools
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5LinguistTools)

Requires: linuxsampler

%description
QSampler is a LinuxSampler GUI front-end application written in
C++ around the Qt5 toolkit using Qt Designer. At the moment it
just wraps as a client reference interface for the LinuxSampler
Control Protocol (LSCP).

%prep
%setup -q

%build
%cmake

%make_build

%install
%make_install -C build

desktop-file-install \
	--remove-key="X-SuSE-translate" \
	--remove-key="Version" \
	--set-key=Exec --set-value="%{name}" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-%{name}-session.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-%{name}-session.svg
%{_datadir}/%{name}/
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/*
%{_mandir}/*/man1/qsampler.1.*
