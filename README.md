# TYPHOON-3
ADSB &amp; ATC Interceptor for SIGINT (Signals Intelligence) &amp; IMINT (Imagery Intelligence) Missions.

Bêta version 3.0
Developped and maintained by [@DK27ss](https://github.com/DK27ss)

## Description:

Typhoon 3 is software that allows the interception of signals using an open-source ADSB (Automatic Dependent Surveillance-Broadcast) decoder and transcribes them onto an interactive map. 
It also intercepts ATC (Air-Traffic-Control) communications, also sourced openly, and displays their locations on an interactive map.

               -               -           PRIVATE & RESTRICTED USAGE ONLY !
              -  -           -  -  
              - -  -  ---  -  - -     Welcome to TYPHOON ©️ (v3.0)
              -  -    ---    -  -   
               -     -- --     -     Framework for intercept
                     -+ +-             ATC (Air-Traffic-Control) &
                    - +++ -               ADSB (Automatic-Dependent-Surveillance–Broadcast) &
                   --     --                 ACARS (Aircraft-Communication-Addressing-Reporting-System).
                   -  +++  -      
                  -++     ++-         This framework was developed for
                 --++     ++--              research purposes in collaboration with SUPERPOSE INTELLIGENCE.
               -----------------      

The interactive map supports various analysis methods, such as image overlay, and also provides the ability to draw geometric shapes or make distance measurements and more.

![Capture](https://github.com/user-attachments/assets/8226ac98-80bc-47bc-bd90-7aae0ddcee15)

# Maps features:

The overlay of maps allows for precise analysis of areas and displays the map in geographical mode, adding location information on top. (Sensitive zones are not necessarily blurred on the maps)

![dfgdfg](https://github.com/DK27ss/TYPHOON-2-/assets/134336163/077ad03b-b309-458f-8c3a-1cfef567875e)

    - mountain                                            
    - altitude                                    
    - airports                                         
    - roads              
    - harbours                                                    
    - buildings                                                    
    - restricted areas   

![x c](https://github.com/DK27ss/TYPHOON-2-/assets/134336163/c955881a-cb02-4794-b8d2-50b064bbc1f2)

## ADS-B

// Real-Time traffic & datas

![dump1](https://github.com/DK27ss/TYPHOON-2-/assets/134336163/66d87fa6-b96e-4fa2-a281-b1efa7893864)

## ATC

// Frequency bandwidth

View ATC listening channel frequencies bandwidth according to the stations selected (with MILILITARY)

![ATC](https://github.com/user-attachments/assets/43ac1426-f86f-4ca9-acaa-f3378d35e078)

## Usage:

To install the USB driver for the SDR Dongle :

    sudo apt-get -fym install git cmake build=essential libusb-1.0-0-dev

To download the SDR dongle reception software (the folders will be created and installed automatically) :

     mkdir git
     git clone git://git.osmocom.org/rtl-sdr.git
     cd rtl-sdr
     mkdir build
     cd build
     cmake . -DINSTALL_UDEV_RULES=ON
     sudo make install
     sudo ldconfig
     sudo cp ../rtl-sdr.rules /etc/udev.rules.d/

Warning! In the event of a problem with CMAKE, and if you receive feedback indicating that it is not installed, type the following command to retrieve it, and then pick up where you left off :

     sudo apt-get install cmake

We're now going to disable the DVB driver. This is the driver used to receive television.
It's of no interest to our experiment, as the frequency we'll be listening to is 1090 MHz. Way beyond TV frequencies.
To do this, we need to create an exception file. Let's create it with the following command :

     sudo nano /etc/modprobe.d/rtlsdr.conf

A new black page opens. This is the text editor.
Add the following line to add the DVB receiver to the driver blacklist :

    blacklist dvb_usb_rtl28xxu

To save the file, press CTRL-O and then ENTER.
You can now close the text editor with the cross (or CTRL-X).

Since the DVB driver was probably loaded once during installation, you'll need to remove it before continuing.
Type the following command :

    lsmod | grep dvb_usb_rtl28xxu

The driver and listening software are now installed ^^

To install the required files correctly :

    git clone https://github.com/DK27ss/TYPHOON-3
    cd TYPHOON-3
    python -m venv env
    source env/bin/activate

To launch the parent application (TYPHOON2) :

    python or python3 TYPHOON3.py

To launch the ADSB LISTENER (Dump1090 Decoder) :

    python ./dump1090.py --interactive --net

To view the interactive map on the localhost (127.0.0.1:8080) you can launch it using the map button in the parent application or directly enter the address in a search engine.

# Disclaimer

It is important to note that the use of Software-Defined Radio (SDR) may be subject to local and international regulations. The reception and transmission of radio signals may be governed by telecommunications laws, privacy laws, and other rules specific to each region. Before engaging in any SDR-related activity, it is strongly recommended to comply with the laws in force in your jurisdiction and obtain all necessary permissions. Unauthorized use of SDR may lead to legal sanctions and severe consequences. The information provided here does not constitute legal advice and should not be interpreted as such. Always refer to local laws and consult legal experts to ensure compliance with all applicable regulations.

## About

If you would like to contribute to the development of the project, please contact me on my Telegram @makaki22 

MIT License

Copyright (c) [2025] [SUPERPOSE INT]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
