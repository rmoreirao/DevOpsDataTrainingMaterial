{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Databricks notebook source\n",
    "import sys\n",
    "sys.path.append(\"/databricks/python3/lib/python3.8/site-packages\")\n",
    "\n",
    "# COMMAND ----------\n",
    "\n",
    "import unittest\n",
    "from addcol import *\n",
    "\n",
    "class TestNotebook(unittest.TestCase):\n",
    "\n",
    "  def test_with_status(self):\n",
    "    source_data = [\n",
    "      (\"pete\", \"pan\", \"peter.pan@databricks.com\"),\n",
    "      (\"jason\", \"argonaut\", \"jason.argonaut@databricks.com\")\n",
    "    ]\n",
    "\n",
    "    source_df = spark.createDataFrame(\n",
    "      source_data,\n",
    "      [\"first_name\", \"last_name\", \"email\"]\n",
    "    )\n",
    "\n",
    "    actual_df = with_status(source_df)\n",
    "\n",
    "    expected_data = [\n",
    "      (\"pete\", \"pan\", \"peter.pan@databricks.com\", \"checked\"),\n",
    "      (\"jason\", \"argonaut\", \"jason.argonaut@databricks.com\", \"checked\")\n",
    "    ]\n",
    "\n",
    "    expected_df = spark.createDataFrame(\n",
    "      expected_data,\n",
    "      [\"first_name\", \"last_name\", \"email\", \"status\"]\n",
    "    )\n",
    "\n",
    "    self.assertEqual(expected_df.collect(), actual_df.collect())\n",
    "\n",
    "unittest.main(argv = [''], verbosity = 2, exit = False)"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
