%define debug_package %{nil}

Summary:	High-definition DVD-AUDIO disc creator
Name:		dvda-author
Version:	09.09
Release:	2
License:	GPLv3+
Group:		Archiving/Cd burning
# Repack, drop built binaries etc from upstream tarball
Url:		http://dvd-audio.sourceforge.net/
Source0:	%{name}-%{version}-60.tar.lzma
BuildRequires:	curl
BuildRequires:	help2man
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(sox)
BuildRequires:	pkgconfig(vorbis)
Requires:	cdrkit
Requires:	dvdauthor
Requires:	imagemagick
Requires:	mkisofs
Requires:	mjpegtools

%description
dvda-author creates high-definition DVD-Audio discs with navigable DVD-Video
zone from DVD-Audio zone Supported input audio types: .wav, .flac, .oga,
SoX-supported formats
EXAMPLES
-creates a 3-group DVD-Audio disc (legacy syntax):

dvda-author -g file1.wav file2.flac -g file3.flac -g file4.wav

-creates a hybrid DVD disc with both AUDIO_TS mirroring audio_input_directory
and VIDEO_TS imported from directory VID, outputs disc structure to directory
DVD_HYBRID and links video titleset #2 of VIDEO_TS to AUDIO_TS:

dvda-author -i ~/audio/audio_input_directory -o DVD_HYBRID -V ~/Video/VID -T 2

Both types of constructions can be combined.

%files
%doc %{_datadir}/doc/%{name}/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}/
%{_datadir}/pixmaps/%{name}*.png
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

