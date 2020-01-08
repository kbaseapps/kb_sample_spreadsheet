/*
A KBase module: kb_sample_spreadsheet
*/

module kb_sample_spreadsheet {
    typedef structure {
        string object_type;
        string user_code;
        string output_name;
        string workspace_name;
    } sampleSpreadsheetParams;

    typedef structure {
        string report_name;
        string report_ref;
    } sampleSpreadsheetResults;

    funcdef generate_sample_spreadsheet(sampleSpreadsheetParams params) returns (sampleSpreadsheetResults results) authentication required;

};
