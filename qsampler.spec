Summary:	LinuxSampler GUI front-end application
Name:	qsampler
Version:	1.0.1
Release:	1
License:	GPLv2
Group:	Sound/Midi
Url:		https://qsampler.sourceforge.io/
Source0:	https://sourceforge.net/projects/qsampler/files/qsampler/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:desktop-file-utils
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(gig) >= 4.5.0
BuildRequires:	pkgconfig(lscp)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(xkbcommon-x11)
Requires: linuxsampler

%description
QSampler is a LinuxSampler GUI front-end application written in
C++ around the Qt6 toolkit using Qt Designer. At the moment it
just wraps as a client reference interface for the LinuxSampler
Control Protocol (LSCP).

%files
%{_bindir}/%{name}
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/org.rncbc.%{name}.png
%{_datadir}/icons/hicolor/*x*/mimetypes/org.rncbc.%{name}.application-x-%{name}-session.png
%{_datadir}/icons/hicolor/scalable/apps/org.rncbc.%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/org.rncbc.%{name}.application-x-%{name}-session.svg
%{_datadir}/%{name}/
%{_datadir}/mime/packages/org.rncbc.%{name}.xml
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml
%{_mandir}/man1/%{name}.1.*
%{_mandir}/*/man1/%{name}.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake \
        -DCONFIG_QT6=yes

%make_build


%install
%make_install -C build

desktop-file-edit \
	--remove-key="X-SuSE-translate" \
	--remove-key="Version" \
	--set-key=Exec --set-value="%{name}" \
	%{buildroot}%{_datadir}/applications/org.rncbc.%{name}.desktop
