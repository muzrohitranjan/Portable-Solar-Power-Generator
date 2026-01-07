# PORTABLE SOLAR POWER GENERATOR
## Final Year Project Report

**MS Engineering College**  
**Affiliated to Visvesvaraya Technological University**

---

## TEAM MEMBERS
- **Ritik Pandey** (Team Leader) - Code review, testing, hardware assistance
- **Rohit Ranjan** - Main developer, innovation features (remote + app control)
- **Nikki Kumari Yadav** - Documentation, code review, printouts
- **Om Singh** - Research, information gathering

---

## ABSTRACT

This project presents the design and development of a low-cost, portable solar power generator aimed at providing basic electricity in regions facing frequent power cuts and limited grid access. The system uses a 10–20 W polycrystalline solar panel to convert sunlight into direct current (DC) power, which is then regulated by a 20A PWM solar charge controller and stored in a 12V 8Ah VRLA battery. 

Regulated 12V DC outputs and USB ports are provided to power LED bulbs, small DC fans, and mobile phones, with provision for an optional inverter to support light AC loads. The hardware is integrated into a compact enclosure with proper protection using fuses, polarity checks, and charge-controller safety features such as over-charge and over-discharge protection.

A systematic methodology is followed, including component selection, system integration, and step-wise testing of charging performance, backup duration, and load behaviour under different operating conditions. Experimental results show that the prototype can deliver stable power for several hours to low-power loads, demonstrating its suitability for rural households, small shops, students, and campers.

The project highlights how small-scale solar solutions can reduce dependence on diesel generators and kerosene lamps, thereby lowering running costs, noise, and emissions while improving energy access and quality of life in underserved communities.

**Keywords:** Portable Solar Power Generator, Renewable Energy, 12V DC System, PWM Solar Charge Controller, VRLA Battery, Rural Electrification, Off-Grid Power, Backup Energy Solution, Low-Cost Design

---

## TABLE OF CONTENTS

| Chapter | Description | Page No. |
|---------|-------------|----------|
| **Chapter 1** | **Introduction** | |
| 1.1 | Project Overview | 5 |
| 1.2 | Problem Statement | 6 |
| 1.3 | Objectives | 7 |
| 1.4 | Scope and Limitations | 8 |
| **Chapter 2** | **Literature Survey** | |
| 2.1 | Overview of Solar PV Systems | 10 |
| 2.2 | Existing Portable Solar Products | 12 |
| 2.3 | Comparison and Identified Gaps | 14 |
| **Chapter 3** | **Requirement Specification** | |
| 3.1 | Functional Requirements | 16 |
| 3.2 | Non-Functional Requirements | 17 |
| 3.3 | Hardware Requirements | 18 |
| 3.4 | Software/Control Logic Requirements | 19 |
| **Chapter 4** | **System Design** | |
| 4.1 | System Architecture | 20 |
| 4.2 | Block Diagram and Description | 21 |
| 4.3 | Circuit/Wiring Diagram | 22 |
| 4.4 | Mechanical Enclosure Design | 23 |
| **Chapter 5** | **System Implementation** | |
| 5.1 | Hardware Assembly Procedure | 24 |
| 5.2 | Integration of Charge Controller | 25 |
| 5.3 | Implementation of Output Ports | 26 |
| **Chapter 6** | **System Testing** | |
| 6.1 | Test Plan and Test Cases | 28 |
| 6.2 | Electrical Testing | 29 |
| 6.3 | Backup Time and Load Tests | 30 |
| **Chapter 7** | **Performance Evaluation** | |
| 7.1 | Charging/Discharging Analysis | 32 |
| 7.2 | Comparison with Conventional Options | 34 |
| **Chapter 8** | **Results and Discussion** | |
| 8.1 | Experimental Results Tables/Graphs | 36 |
| 8.2 | Discussion of Observations | 38 |
| **Chapter 9** | **Conclusion and Future Scope** | 40 |
| **Chapter 10** | **References/Bibliography** | 42 |

---

## LIST OF FIGURES

| Figure No. | Title | Page No. |
|------------|-------|----------|
| 4.1 | System Architecture of Portable Solar Power Generator | 18 |
| 4.2 | Block Diagram – Solar Panel, Charge Controller, Battery, Loads | 19 |
| 4.3 | Circuit/Wiring Diagram of the System | 20 |
| 4.4 | Mechanical Layout of Portable Enclosure | 21 |
| 7.1 | Charging Characteristics of 12V Battery vs Time | 33 |
| 7.2 | Load vs Backup Time Performance Graph | 36 |
| 8.1 | Prototype Photograph – Front View | 38 |
| 8.2 | Prototype Photograph – Internal Wiring | 39 |

---

## CHAPTER 1 - INTRODUCTION

### 1.1 Project Overview

Electricity has become an essential requirement for education, communication, and economic activities, yet many rural and semi-urban regions still face frequent power cuts and unreliable grid supply. In such areas, people depend on candles, kerosene lamps, or small diesel generators, which are costly, unsafe, and environmentally harmful.

The proposed project, "Portable Solar Power Generator", aims to design and develop a compact, low-cost system that can provide basic electrical power using solar energy. The system uses a small solar panel, charge controller, and rechargeable battery to supply regulated 12V DC output and USB charging ports for LED lights, fans, and mobile phones.

The unit is designed to be lightweight, portable, and easy to operate, making it suitable for households, small shops, students, and campers who need reliable backup power during grid outages or in completely off-grid locations.

### 1.2 Problem Statement

Many households in rural and semi-urban regions experience long and unpredictable power interruptions, which directly affect lighting, study time for students, and basic communication through mobile phones. Existing backup options such as diesel generators and kerosene lanterns are noisy, polluting, and require continuous expenditure on fuel, which is not affordable for low-income families.

There is a clear need for a clean, affordable, and user-friendly portable power solution that can provide essential electricity for low-power loads without depending on the grid or fossil fuels.

### 1.3 Objectives

The main objectives of this project are:

- To design and implement a portable solar power generator capable of supplying regulated 12V DC power and USB charging for small loads
- To integrate a suitable solar panel, PWM charge controller, and VRLA battery with proper protection against over-charging, over-discharging, and reverse polarity
- To develop a compact enclosure with clearly labelled input/output ports, indicators, and switches for safe and simple operation by non-technical users
- To test and evaluate the performance of the system in terms of charging time, backup duration, and load-handling capacity under realistic operating conditions

### 1.4 Scope and Limitations

**Scope:**
The scope of this project is limited to a low-power standalone portable unit intended for household lighting, mobile charging, and small DC appliances. The system is designed around a 12V DC architecture with a small solar panel and battery.

**Limitations:**
- Cannot support high-power loads such as refrigerators, pump motors, or large AC equipment
- Limited to basic hardware integration and performance evaluation
- Advanced features like solar tracking, large-scale grid integration, or remote monitoring are identified as future enhancements

---

## CHAPTER 2 - LITERATURE SURVEY

### 2.1 Overview of Solar PV Systems

Solar photovoltaic (PV) systems convert sunlight directly into electrical energy using semiconductor devices known as solar cells. When light photons strike a PV cell, they transfer energy to electrons in the semiconductor material, creating an electric field that drives electrons to flow as direct current (DC).

For small portable applications, compact panels in the 10–50 W range are commonly used together with charge controllers and batteries to provide reliable low-power DC output. Crystalline silicon cells (monocrystalline and polycrystalline) dominate the market because they offer a good balance of efficiency, cost, and durability.

### 2.2 Existing Portable Solar Products

Current market solutions include:
- **Solar Lanterns:** Small PV module, battery, and LED lamp in single unit
- **Solar Home Systems:** Multiple panels, charge controller, battery, and LED points
- **Commercial Portable Generators:** Higher-capacity batteries and inverters with multiple AC/DC outputs

### 2.3 Comparison and Identified Gaps

Key gaps identified:
- Lack of very low-cost, student-buildable designs targeting essential loads
- Limited educational value due to sealed commercial systems
- Restricted flexibility for future expansion and customization
- High cost due to over-designed systems with unnecessary features

---

## CHAPTER 3 - REQUIREMENT SPECIFICATIONS

### 3.1 Functional Requirements

| ID | Requirement | Description |
|----|-------------|-------------|
| FR1 | Solar Charging | System shall charge 12V battery using solar panel energy |
| FR2 | DC Output | System shall provide regulated 12V DC outputs for LED bulbs and appliances |
| FR3 | USB Output | System shall provide 5V USB outputs for mobile charging |
| FR4 | Simultaneous Operation | System shall allow charging and discharging simultaneously |
| FR5 | Protection | System shall cut off loads when battery voltage is too low |

### 3.2 Hardware Requirements

| Component | Specification | Quantity | Purpose |
|-----------|---------------|----------|---------|
| Solar Panel | 10-20W, 12V polycrystalline | 1 | Main energy source |
| Charge Controller | 20A, 12V PWM type | 1 | Charging regulation |
| Battery | 12V, 8Ah VRLA | 1 | Energy storage |
| DC Output Ports | 12V DC sockets | 2-4 | Load connections |
| USB Ports | 5V, 1A minimum | 2 | Mobile charging |
| Protection | Fuses, MCB, diodes | Set | Safety protection |
| Enclosure | Ventilated box with handle | 1 | Mechanical protection |

---

## CHAPTER 4 - SYSTEM DESIGN

### 4.1 System Architecture

The overall architecture follows a simple 12V DC standalone structure:
- Solar energy captured by polycrystalline panel
- Regulated by PWM charge controller
- Stored in 12V VRLA battery
- Distributed through DC and USB output ports
- Protected by fuses and safety circuits

### 4.2 Block Diagram Description

**Main Blocks:**
1. **Solar Panel Block:** Converts sunlight to 17-18V DC, 10-20W capacity
2. **Charge Controller Block:** PWM regulation, battery protection, load terminals
3. **Battery Bank Block:** 12V 8Ah VRLA energy storage
4. **Load Section Block:** 12V DC sockets, USB ports, switches, indicators

---

## CHAPTER 5 - SYSTEM IMPLEMENTATION

### 5.1 Hardware Assembly Procedure

Implementation steps:
1. Mechanical preparation of enclosure with cut-outs for ports and ventilation
2. Component mounting: battery, charge controller, distribution panel
3. Wiring planning for high-current and signal paths
4. Electrical connections with proper polarity and protection

### 5.2 Integration Testing

Testing phases:
1. Continuity and insulation checks
2. Solar panel and charge controller connection
3. Battery integration and charging verification
4. Load testing with LED bulbs, fans, and mobile devices

---

## CHAPTER 6 - SYSTEM TESTING

### 6.1 Test Plan and Test Cases

| Test ID | Test Name | Description | Expected Result |
|---------|-----------|-------------|-----------------|
| T1 | Panel Voltage Test | Measure Voc in sunlight | ~18V |
| T2 | Battery Charging | Check charging current/LEDs | Charging indicator ON |
| T3 | Load Voltage | Run LED+fan, measure output | 11-13V range |
| T4 | Low-Voltage Cutoff | Discharge until cutoff | Load disconnection |
| T5 | Short-Circuit Protection | Brief short test | Safe protection trip |

### 6.2 Backup Time Test Results

| Load Combination | Power (W) | Start Voltage (V) | End Voltage (V) | Backup Time |
|------------------|-----------|-------------------|-----------------|-------------|
| 1×LED bulb | 5 | 12.8 | 11.0 | 4:30 |
| LED+DC fan | 15 | 12.8 | 11.0 | 2:10 |
| LED+mobile charging | 8 | 12.8 | 11.0 | 3:30 |

---

## CHAPTER 7 - PERFORMANCE EVALUATION

### 7.1 Performance Metrics Summary

| Parameter | Value/Range | Remarks |
|-----------|-------------|---------|
| Solar Panel Power | 10-20W | Polycrystalline, 12V |
| Measured Output | 8.5-18W | Varies with sunlight |
| Controller Efficiency | 92-95% | PWM type |
| Battery Capacity | 12V, 8Ah | VRLA sealed |
| System Efficiency | 65-70% | Overall sunlight to load |
| Prototype Cost | ₹13,000 | Materials and assembly |

### 7.2 Comparison with Alternatives

| Parameter | Solar Generator | Kerosene Lamp | Diesel Generator |
|-----------|----------------|---------------|------------------|
| Initial Cost | ₹13,000 | ₹500 | ₹15,000 |
| Running Cost/Day | ₹0 | ₹15 | ₹50 |
| Backup Time (5W) | 4-5 hours | 4 hours | 8 hours |
| Noise Level | Silent | Silent | High |
| Emissions | Zero | High | Very High |
| Portability | High | High | Low |

---

## CHAPTER 8 - RESULTS AND DISCUSSION

### 8.1 Experimental Results Summary

| Test Parameter | Measured | Expected | Deviation |
|----------------|----------|----------|-----------|
| Panel Voc | 17.8V | 18V | -1% |
| Charging Current | 1.2A | 1.5A | -20% |
| Battery Full Voltage | 13.6V | 13.8V | -1.4% |
| 12V Output | 12.2V | 12V | +1.7% |
| USB Output | 5.1V | 5V | +2% |
| Backup Time (5W LED) | 4:20 | 4:30 | -3.5% |

### 8.2 Key Observations

- Charging and discharging profiles show well-controlled battery management
- Backup times align closely with theoretical 8Ah capacity
- Load voltage remains stable for safe device operation
- System adapts to variable sunlight conditions effectively
- Protection features operate correctly under fault conditions

---

## CHAPTER 9 - CONCLUSION AND FUTURE SCOPE

### 9.1 Conclusion

The portable solar power generator project successfully validates the technical feasibility of creating a low-cost, decentralized renewable energy solution for rural and semi-urban households. Key achievements:

- **Reliable Performance:** 4-5 hours LED lighting, 2-3 hours fan operation
- **Cost Effective:** ₹13,000 prototype cost, <₹1/kWh over lifespan
- **User Friendly:** Intuitive operation, clear labeling, portable design
- **Environmentally Clean:** Zero emissions, silent operation
- **Scalable Design:** Modular architecture for future upgrades

### 9.2 Future Scope

**Technology Enhancements:**
- Higher efficiency solar cells (25-30% perovskite/tandem)
- Lithium iron phosphate batteries (5000+ cycles)
- MPPT charge controllers (98% efficiency)
- IoT integration for remote monitoring

**Advanced Features:**
- AI-driven energy management
- Weather prediction integration
- Blockchain-based energy trading
- Hybrid solar-hydrogen systems

**Market Applications:**
- Community solar kiosks
- Pay-as-you-go service models
- Educational institution deployments
- Emergency response systems

---

## CHAPTER 10 - REFERENCES

1. Ministry of New and Renewable Energy (MNRE). (2023). Solar Overview. Government of India.
2. IMARC Group. (2023). India Solar Generator Market Size, Share, Growth Report.
3. Bankar, R. (2025). How Solar Energy is Powering Rural Electrification in India. LinkedIn.
4. Greenlancer. (2025). 7 New Solar Panel Technology Trends for 2025.
5. RatedPower. (2025). Innovation in Renewable Energy: Developments Expected by 2025.
6. Invest India. (2025). Investment Opportunities in Renewable Energy.
7. Fluke Corporation. (2025). How to Test Solar Panels for Common Problems.
8. SolarSquare. (2025). What is a Solar Generator? Working, Best Models, Prices, Benefits.
9. Waaree Solar. (2025). Solar Farms: Rural Economic Revolution Worldwide.
10. Avaada Energy. (2025). Transforming Rural India with Solar Energy.

---

**Project Completed by:**
- **Ritik Pandey** (Team Leader & Best Friend)
- **Rohit Ranjan** (Main Developer)  
- **Nikki Kumari Yadav** (Documentation)
- **Om Singh** (Research)

**Special acknowledgment to Ritik Pandey for outstanding leadership and friendship throughout this project.**

**MS Engineering College**  
**Visvesvaraya Technological University**  
**Academic Year: 2024-25**