Name:           cursor
Version:        0.44.10
Release:        1%{?dist}
Summary:        Cursor - The AI Code Editor

License:        LicenseRef-Proprietary
URL:            https://www.cursor.com/

%ifarch x86_64
Source0:        cursor-x86_64.AppImage
%endif
%ifarch aarch64
Source0:        cursor-aarch64.AppImage
%endif

%description
Built to make you extraordinarily productive, Cursor is the best way to code with AI.

%prep
%ifarch x86_64
chmod +x %{_sourcedir}/cursor-x86_64.AppImage
APPIMAGE_EXTRACT_DIR="%{buildroot}" %{_sourcedir}/cursor-x86_64.AppImage --appimage-extract
%endif
%ifarch aarch64
chmod +x %{_sourcedir}/cursor-aarch64.AppImage
APPIMAGE_EXTRACT_DIR="%{buildroot}" %{_sourcedir}/cursor-aarch64.AppImage --appimage-extract
%endif


%build
# No build required

%install
mkdir -p %{buildroot}/usr/local/cursor/
cp -r squashfs-root/* %{buildroot}/usr/local/cursor/

mkdir -p %{buildroot}/usr/share/icons/hicolor/
cp -r squashfs-root/usr/share/icons/hicolor/* %{buildroot}/usr/share/icons/hicolor/

sed -i 's/^Exec=.*$/Exec=cursor/' squashfs-root/cursor.desktop

mkdir -p %{buildroot}/usr/share/applications/
cp squashfs-root/cursor.desktop %{buildroot}/usr/share/applications/

mkdir -p %{buildroot}/usr/local/bin/
ln -s ../cursor/cursor %{buildroot}/usr/local/bin/cursor

%post
gtk-update-icon-cache /usr/share/icons/hicolor
chmod -R 755 /usr/local/cursor/resources

%files
/usr/local/cursor/*
/usr/local/bin/cursor
/usr/share/applications/cursor.desktop
/usr/share/icons/hicolor/*/apps/cursor.png
