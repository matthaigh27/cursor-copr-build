Name:           cursor
Version:        0.50.4
Release:        1%{?dist}
Summary:        Cursor - The AI Code Editor

License:        LicenseRef-Proprietary  # Update according to the actual license
URL:            https://www.cursor.com/
Source0:        Cursor-0.50.4-x86_64.AppImage

BuildArch:      x86_64
ExclusiveArch:  x86_64
Requires:       ffmpeg

%description
Built to make you extraordinarily productive, Cursor is the best way to code with AI.

%prep
# No prep required

%build
# No build required

%install
chmod +x %{SOURCE0}
%{SOURCE0} --appimage-extract

mkdir -p %{buildroot}/usr/local/cursor/
cp -r squashfs-root/* %{buildroot}/usr/local/cursor/

mkdir -p %{buildroot}/lib64
cp squashfs-root/usr/share/cursor/libffmpeg.so %{buildroot}/lib64/libffmpeg.so

mkdir -p %{buildroot}/usr/share/icons/hicolor/
cp -r squashfs-root/usr/share/icons/hicolor/* %{buildroot}/usr/share/icons/hicolor/

sed -i 's/^Exec=.*$/Exec=cursor/' squashfs-root/cursor.desktop

mkdir -p %{buildroot}/usr/share/applications/
cp squashfs-root/cursor.desktop %{buildroot}/usr/share/applications/

mkdir -p %{buildroot}/usr/local/bin/
ln -s ../cursor/AppRun %{buildroot}/usr/local/bin/cursor

%post
gtk-update-icon-cache /usr/share/icons/hicolor
chmod -R 755 /usr/local/cursor/resources

%files
/lib64/libffmpeg.so
/usr/local/cursor/*
/usr/local/bin/cursor
/usr/share/applications/cursor.desktop
/usr/share/icons/hicolor/*/apps/cursor.png

%changelog
* Sat May 17 2025 Andrea Manenti <andrea.manenti@proton.me> - 0.50.4-1
  - Updated version
* Sat Apr 26 2025 Andrea Manenti <andrea.manenti@proton.me> - 0.49.6-1
  - Updated version
* Fri Apr 18 2025 Andrea Manenti <andrea.manenti@proton.me> - 0.48.9-1
  - Updated paths and added ffmpeg dependency
