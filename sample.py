from OperatingDT import *

query = """
{
  stores(filter: {id: {operator: "eq", value: "36", type: "int"}})
  {
    shelves
    {
      id,
      externalReferenceId

      shelfLayers
      {
        shelfId
        level
        id
        externalReferenceId
      }
    }
  }
}
"""
print POSTGRAPHQL(query)
