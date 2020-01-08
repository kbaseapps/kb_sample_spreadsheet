# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
from pprint import pprint

from installed_clients.KBaseReportClient import KBaseReport

from kb_sample_spreadsheet.utils.SampleSpreadsheetGenerator import SampleSpreadsheetGenerator
#END_HEADER


class kb_sample_spreadsheet:
    '''
    Module Name:
    kb_sample_spreadsheet

    Module Description:
    A KBase module: kb_sample_spreadsheet
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.scratch_dir = os.path.abspath(config['scratch'])
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def generate_sample_spreadsheet(self, ctx, params):
        """
        :param params: instance of type "sampleSpreadsheetParams" ->
           structure: parameter "object_type" of String, parameter
           "user_code" of String, parameter "output_name" of String,
           parameter "workspace_name" of String
        :returns: instance of type "sampleSpreadsheetResults" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: results
        #BEGIN generate_sample_spreadsheet
        sample_spreadsheet_generator=SampleSpreadsheetGenerator(
          self.scratch_dir,
          self.callback_url,
          ctx
        )
        results=sample_spreadsheet_generator.generate(params);
        #END generate_sample_spreadsheet

        # At some point might do deeper type checking...
        if not isinstance(results, dict):
            raise ValueError('Method generate_sample_spreadsheet return value ' +
                             'results is not type dict as required.')
        # return the results
        return [results]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
