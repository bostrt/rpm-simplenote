Name:           simplenote
Version:        1.0.8
Release:        1
Summary:        Simplenote.com desktop client

License:        GPLv2
URL:            https://simplenote.com/downloads/
Source0:        https://github.com/Automattic/simplenote-electron/archive/v%{version}.tar.gz
Source1:        config.json
#Patch0:         remove-react-popover.patch

%global __requires_exclude ^libffmpeg.*$
%global __requires_exclude %__requires_exclude|^libgcrypt.*$
%global __requires_exclude %__requires_exclude|^libnode.*$

BuildRequires: make
BuildRequires: nodejs >= 1:4.4.5
BuildRequires: which
BuildRequires: nodejs-packaging
BuildRequires: npm
Requires: nodejs >= 1:4.4.5

%global debug_package %{nil}

%description
A simplenote.com client packaged in Electron.

%prep
%setup -q -n simplenote-electron-%{version}
#%patch0 -p1
cp %SOURCE1 $RPM_BUILD_DIR/simplenote-electron-%{version}

%build
npm -g -q --production --prefix="${RPM_BUILD_ROOT}%{_prefix}" install
make linux

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/simplenote
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/simplenote

install -m 644 $RPM_BUILD_DIR/simplenote-electron-%{version}/resources/linux/simplenote.desktop $RPM_BUILD_ROOT%{_datadir}/applications/simplenote.desktop
install -m 644 $RPM_BUILD_DIR/simplenote-electron-%{version}/release/Simplenote-linux-x64/Simplenote.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/simplenote.png
cp -r $RPM_BUILD_DIR/simplenote-electron-%{version}/release/Simplenote-linux-x64/* $RPM_BUILD_ROOT%{_datadir}/simplenote/

# Rename executable to match .desktop file
mv $RPM_BUILD_ROOT%{_datadir}/simplenote/Simplenote $RPM_BUILD_ROOT%{_datadir}/simplenote/simplenote

%files
%defattr(-, root, root, -)
%{_datadir}/applications/simplenote.desktop
%{_datadir}/pixmaps/simplenote.png
%{_datadir}/simplenote/

%changelog
* Wed Mar 29 2017 Robert Bost 1.0.8-1
- new package built with tito

