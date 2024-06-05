# TYPHOON-2
ADSB &amp; ATC Interceptor for SIGINT (Signals Intelligence)&amp; IMINT (Imagery Intelligence) Missions.

Typhoon 2 is software that allows the interception of signals using an open-source ADSB (Automatic Dependent Surveillance-Broadcast) decoder and transcribes them onto an interactive map. 
It also intercepts ATC (Air-Traffic-Control) communications, also sourced openly, and displays their locations on an interactive map.

The interactive map supports various analysis methods, such as image overlay, and also provides the ability to draw geometric shapes or make distance measurements and more.

# DISCLAIMER ⚠️

It is important to note that the use of Software-Defined Radio (SDR) may be subject to local and international regulations. The reception and transmission of radio signals may be governed by telecommunications laws, privacy laws, and other rules specific to each region. Before engaging in any SDR-related activity, it is strongly recommended to comply with the laws in force in your jurisdiction and obtain all necessary permissions. Unauthorized use of SDR may lead to legal sanctions and severe consequences. The information provided here does not constitute legal advice and should not be interpreted as such. Always refer to local laws and consult legal experts to ensure compliance with all applicable regulations.

![dump1](https://github.com/DK27ss/TYPHOON-2-/assets/134336163/66d87fa6-b96e-4fa2-a281-b1efa7893864)

![Capture2](https://github.com/DK27ss/TYPHOON-2-/assets/134336163/c433e357-fb3d-4c50-b140-42ee0bc9c0d5)

# INVESTIGATION 🔍

The overlay of maps allows for precise analysis of areas and displays the map in geographical mode, adding location information on top. (Sensitive zones are not necessarily blurred on the maps)

![dfgdfg](https://github.com/DK27ss/TYPHOON-2-/assets/134336163/077ad03b-b309-458f-8c3a-1cfef567875e)

this mode provides very precise information (mountain names, altitude, airports, roads, harbours, buildings) and more..

![x c](https://github.com/DK27ss/TYPHOON-2-/assets/134336163/c955881a-cb02-4794-b8d2-50b064bbc1f2)

# USAGE ⚙️

To install the required files correctly :

    git clone https://github.com/DK27ss/TYPHOON-2
    cd TYPHOON-2
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt

To launch the parent application (TYPHOON2) :

    python or python3 TYPHOON2.py

To launch the ADSB LISTENER (Dump1090 Decoder) :

    python ./dump1090.py --interactive --net

To view the interactive map on the localhost (127.0.0.1:8080) you can launch it using the map button in the parent application or directly enter the address in a search engine.

# ABOUT 📑

MIT License

Copyright (c) [2024] [SUPERPOSE INT]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
