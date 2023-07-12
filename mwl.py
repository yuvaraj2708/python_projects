import requests

def fetch_worklist():
    base_url = "http://103.170.114.135:8080/dcm4chee-arc/aets/WORKLIST/rs/mwlitems"

    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            worklist = response.json()
            return worklist
        else:
            print(f"Failed to fetch worklist. Response status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

    return None

def display_worklist(worklist):
    print("Worklist:")
    print("------------------------")

    for item in worklist:
        patient_id = item.get("00100020", {}).get("Value", [""])[0]
        gender = item.get("00100040", {}).get("Value", [""])[0]
        Modality = item.get("00080060", {}).get("Value", [""])[0]
        patient_name = item.get("00100010", {}).get("Value", [""])[0]
        AccessionNumber = item.get("00080050", {}).get("Value", [""])[0]
        InstitutionName = item.get("00080080", {}).get("Value", [""])[0]
        InstitutionCodeSequence = item.get("00080082", {}).get("Value", [""])[0]
        CodeValue = item.get("00080100", {}).get("Value", [""])[0]
        CodingSchemeDesignator = item.get("00080102", {}).get("Value", [""])[0]
        CodeMeaning = item.get("00080104", {}).get("Value", [""])[0]
        ReferringPhysicianName = item.get("00080090", {}).get("Value", [""])[0]
        MedicalAlerts = item.get("00102000", {}).get("Value", [""])[0]
        StudyInstanceUID = item.get("0020000D", {}).get("Value", [""])[0]
        RequestingPhysician = item.get("00321032", {}).get("Value", [""])[0]
        RequestedProcedureDescription = item.get("00321060", {}).get("Value", [""])[0]
        AdmissionID = item.get("00380010", {}).get("Value", [""])[0]
        IssuerofAdmissionIDSequence = item.get("00380014", {}).get("Value", [""])[0]
        LocalNamespaceEntityID = item.get("00400031", {}).get("Value", [""])[0]
        RouteofAdmissions = item.get("00380016", {}).get("Value", [""])[0]
        OrderPlacerIdentifierSequence = item.get("00400026", {}).get("Value", [""])[0]
        LocalNamespaceEntityID = item.get("00400031", {}).get("Value", [""])[0]
        OrderFillerIdentifierSequence = item.get("00400027", {}).get("Value", [""])[0]
        LocalNamespaceEntityID = item.get("00400031", {}).get("Value", [""])[0]
        ScheduledProcedureStepSequence = item.get("00400100", {}).get("Value", [""])[0]
        ScheduledStationAETitle = item.get("00400001", {}).get("Value", [""])[0]
        ScheduledProcedureStepStartDate = item.get("00400002", {}).get("Value", [""])[0]
        ScheduledProcedureStepStartTime = item.get("00400003", {}).get("Value", [""])[0]
        ScheduledPerformingPhysicianName = item.get("00400006", {}).get("Value", [""])[0]
        ScheduledProcedureStepDescription = item.get("00400007", {}).get("Value", [""])[0]
        ScheduledProtocolCodeSequence = item.get("00400008", {}).get("Value", [""])[0]
        CodeValue = item.get("00080100", {}).get("Value", [""])[0]
        CodingSchemeDesignator = item.get("00080102", {}).get("Value", [""])[0]
        CodeMeaning = item.get("00080104", {}).get("Value", [""])[0]
        ScheduledProcedureStepID = item.get("00400009", {}).get("Value", [""])[0]
        ScheduledStationName = item.get("00400010", {}).get("Value", [""])[0]
        ScheduledProcedureStepLocation = item.get("00400011", {}).get("Value", [""])[0]
        ScheduledProcedureStepStatus = item.get("00400020", {}).get("Value", [""])[0]
        RequestedProcedureID = item.get("00401001", {}).get("Value", [""])[0]
        RequestedProcedurePriority = item.get("00401003", {}).get("Value", [""])[0]
        PatientTansportArrangements = item.get("00401004", {}).get("Value", [""])[0]
        PlacerOrderNumberImagingServiceRequest = item.get("00402016", {}).get("Value", [""])[0]
        FillerOrderNumberImagingServiceRequest = item.get("00402017", {}).get("Value", [""])[0]

        


        print(f"Patient ID: {patient_id}")
        print(f"Gender: {gender}")
        print(f"Modality: {Modality}")
        print(f"patient_name: {patient_name}")
        print(f"AccessionNumber: { AccessionNumber}")
        print(f"InstitutionName: {InstitutionName}")
        print(f"InstitutionCodeSequence: {InstitutionCodeSequence}")
        print(f"CodeValue: {CodeValue}")
        print(f"CodingSchemeDesignator: {CodingSchemeDesignator}")
        print(f"CodeMeaning: {CodeMeaning}")
        print(f"ReferringPhysicianName: {ReferringPhysicianName}")
        print(f"MedicalAlerts: {MedicalAlerts}")
        print(f"StudyInstanceUID: {StudyInstanceUID}")
        print(f"RequestingPhysician: {RequestingPhysician}")
        print(f"RequestedProcedureDescription: {RequestedProcedureDescription}")
        print(f"AdmissionID: {AdmissionID}")
        print(f"IssuerofAdmissionIDSequence: {IssuerofAdmissionIDSequence}")
        print(f"LocalNamespaceEntityID: {LocalNamespaceEntityID}")
        print(f"RouteofAdmissions: {RouteofAdmissions}")
        print(f"OrderPlacerIdentifierSequence: {OrderPlacerIdentifierSequence}")
        print(f"OrderFillerIdentifierSequence: {OrderFillerIdentifierSequence}")
        print(f"ScheduledProcedureStepSequence: {ScheduledProcedureStepSequence}")
        print(f"ScheduledStationAETitle: {ScheduledStationAETitle}")
        print(f"ScheduledProcedureStepStartDate: {ScheduledProcedureStepStartDate}")
        print(f"ScheduledProcedureStepID: {ScheduledProcedureStepID}")
        print(f"ScheduledProcedureStepStartTime: {ScheduledProcedureStepStartTime}")
        print("------------------------")

# Fetch and display the worklist
worklist = fetch_worklist()
if worklist:
    display_worklist(worklist)



 










