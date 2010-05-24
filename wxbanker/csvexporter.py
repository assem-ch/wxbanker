#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, cStringIO

class CsvExporter:
    """Iterate through the list of transactions for an account and
    exort to a CSV file."""
    
    @staticmethod
    def Generate(model, delimiter=",", quotechar="'"):
        """Generate the CSV string."""
        result = cStringIO.StringIO()
        writer = csv.writer(result, delimiter=delimiter, quotechar=quotechar)
        writer.writerow(['Account', 'Description', 'Amount', 'Date'])

        # Iterate through transaction list, write rows.
        for account in model.Accounts:
            for transaction in account.Transactions:
                row = [account.Name, transaction.GetDescription(), transaction.GetAmount(), transaction.GetDate()]
                writer.writerow(row)
                
        return result.getvalue()
    
    @staticmethod
    def Export(exportPath):
        # Open the CSV file for writing, write headers.
        exportFile = open(exportPath, 'w')
        # Generate the contents.
        result = CsvExporter.Generate()
        # Write it.
        exportFile.write(result)