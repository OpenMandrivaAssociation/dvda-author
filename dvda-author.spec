Summary:	High-definition DVD-AUDIO disc creator
Name:		dvda-author
Version:	09.09
Release:	4
License:	GPLv3
Group:		Archiving/Cd burning
Source0:	%{name}-%{version}-60.tar.lzma
URL:		http://dvd-audio.sourceforge.net/
BuildRequires:	curl sox-devel
BuildRequires:	oggvorbis-devel libflac-devel help2man
Requires:	dvdauthor mkisofs cdrkit
Requires:	mjpegtools imagemagick

%define debug_package %{nil}

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
%makeinstall_std

%clean 

%files
%defattr(-,root, root)
%doc %{_datadir}/doc/%{name}/*
%{_bindir}/%{name}
%dir %{_datadir}/applications/%{name}
%{_datadir}/applications/%{name}/*
%{_datadir}/pixmaps/%{name}*.png
%{_mandir}/man1/%{name}.1*



%changelog
* Tue Aug 14 2012 Denis Silakov <dsilakov@mandriva.org> 09.09-3
+ Revision: 814784
- Dropped unneeded dependency

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 09.09-2mdv2011.0
+ Revision: 610302
- rebuild

* Fri Dec 25 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 09.09-1mdv2010.1
+ Revision: 482263
- import dvda-author


* Fri Dec 25 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 09.09-1
- initial release
