Summary:	High-definition DVD-AUDIO disc creator
Name:		dvda-author
Version:	09.09
Release:	%mkrel 1
License:	GPLv3
Group:		Archiving/Cd burning
Source0:	%{name}-%{version}-60.tar.lzma
URL:		http://dvd-audio.sourceforge.net/
BuildRequires:	curl sox-devel
BuildRequires:	oggvorbis-devel libflac-devel help2man
Requires:	dvdauthor spumux mkisofs cdrkit
Requires:	mjpegtools ImageMagick
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root, root)
%doc %{_datadir}/doc/%{name}/*
%{_bindir}/%{name}
%dir %{_datadir}/applications/%{name}
%{_datadir}/applications/%{name}/*
%{_datadir}/pixmaps/%{name}*.png
%{_mandir}/man1/%{name}.1*

