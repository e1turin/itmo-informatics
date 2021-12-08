' Макрос составил Тюрин Иван

Sub Кнопка2_Щелчок()
	
	' Определяем переменные
	Dim rng As Range
	
	' Выбираем диапазон
	Set rng = ActiveWorkbook.Worksheets("Ëèñò1").Range("G4", "V7")
	
	' Очищаем форматирование
    	rng.FormatConditions.Delete

End Sub
