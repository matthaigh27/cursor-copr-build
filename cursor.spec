Name:           cursor
Version:        <version>
Release:        1%{?dist}
Summary:        Cursor - The AI Code Editor

License:        LicenseRef-Proprietary  # Update according to the actual license
URL:            https://www.cursor.com/
Source0:        <source>

ExclusiveArch:  <arch>

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
