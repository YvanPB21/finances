"""
Rutas de la aplicación Flask
"""
from flask import Blueprint, render_template, request, jsonify
from app.models import (
    SavingsAccount, CreditCard, Cash, SavingsGoal, Loan, CardInstallment, MonthlyBudget, PersonalLoan, FinancialSummary
)

main_bp = Blueprint('main', __name__)

# Ruta principal - Dashboard
@main_bp.route('/')
def index():
    """Página principal con dashboard"""
    return render_template('dashboard.html')

@main_bp.route('/accounts')
def accounts():
    """Página de cuentas de ahorro"""
    return render_template('accounts.html')

@main_bp.route('/cards')
def cards():
    """Página de tarjetas de crédito"""
    return render_template('cards.html')

@main_bp.route('/cash')
def cash_page():
    """Página de efectivo"""
    return render_template('cash.html')

@main_bp.route('/goals')
def goals():
    """Página de metas de ahorro"""
    return render_template('goals.html')

@main_bp.route('/loans')
def loans():
    """Página de préstamos"""
    return render_template('loans.html')

@main_bp.route('/budget')
def budget():
    """Página de balance mensual"""
    return render_template('budget.html')

@main_bp.route('/personal-loans')
def personal_loans():
    """Página de préstamos personales"""
    return render_template('personal_loans.html')

# API Endpoints - Summary
@main_bp.route('/api/summary')
def api_summary():
    """Obtiene el resumen financiero completo"""
    try:
        summary = FinancialSummary.get_summary()
        return jsonify(summary), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Endpoints - Savings Accounts
@main_bp.route('/api/accounts', methods=['GET'])
def api_get_accounts():
    """Obtiene todas las cuentas de ahorro"""
    try:
        accounts = SavingsAccount.get_all()
        return jsonify(accounts), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/accounts', methods=['POST'])
def api_create_account():
    """Crea una nueva cuenta de ahorro"""
    try:
        data = request.get_json()
        account_id = SavingsAccount.create(data)
        return jsonify({'id': account_id, 'message': 'Cuenta creada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/accounts/<account_id>', methods=['PUT'])
def api_update_account(account_id):
    """Actualiza una cuenta de ahorro"""
    try:
        data = request.get_json()
        SavingsAccount.update(account_id, data)
        return jsonify({'message': 'Cuenta actualizada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/accounts/<account_id>', methods=['DELETE'])
def api_delete_account(account_id):
    """Elimina una cuenta de ahorro"""
    try:
        SavingsAccount.delete(account_id)
        return jsonify({'message': 'Cuenta eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Endpoints - Credit Cards
@main_bp.route('/api/cards', methods=['GET'])
def api_get_cards():
    """Obtiene todas las tarjetas de crédito"""
    try:
        cards = CreditCard.get_all()
        return jsonify(cards), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/cards', methods=['POST'])
def api_create_card():
    """Crea una nueva tarjeta de crédito"""
    try:
        data = request.get_json()
        card_id = CreditCard.create(data)
        return jsonify({'id': card_id, 'message': 'Tarjeta creada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/cards/<card_id>', methods=['PUT'])
def api_update_card(card_id):
    """Actualiza una tarjeta de crédito"""
    try:
        data = request.get_json()
        CreditCard.update(card_id, data)
        return jsonify({'message': 'Tarjeta actualizada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/cards/<card_id>', methods=['DELETE'])
def api_delete_card(card_id):
    """Elimina una tarjeta de crédito"""
    try:
        CreditCard.delete(card_id)
        return jsonify({'message': 'Tarjeta eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Endpoints - Card Installments (Cuotas)
@main_bp.route('/api/cards/<card_id>/installments', methods=['GET'])
def api_get_card_installments(card_id):
    """Obtiene todas las compras en cuotas de una tarjeta"""
    try:
        installments = CardInstallment.get_all_by_card(card_id)
        return jsonify(installments), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/cards/<card_id>/installments', methods=['POST'])
def api_create_card_installment(card_id):
    """Crea una nueva compra en cuotas"""
    try:
        data = request.get_json()
        data['card_id'] = card_id
        installment_id = CardInstallment.create(data)
        return jsonify({'id': installment_id, 'message': 'Compra en cuotas registrada'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/cards/<card_id>/installments/<installment_id>', methods=['PUT'])
def api_update_card_installment(card_id, installment_id):
    """Actualiza una compra en cuotas"""
    try:
        data = request.get_json()
        CardInstallment.update(installment_id, data)
        return jsonify({'message': 'Compra actualizada'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/cards/<card_id>/installments/<installment_id>', methods=['DELETE'])
def api_delete_card_installment(card_id, installment_id):
    """Elimina una compra en cuotas"""
    try:
        CardInstallment.delete(installment_id)
        return jsonify({'message': 'Compra eliminada'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/cards/<card_id>/monthly-payment', methods=['GET'])
def api_get_monthly_payment(card_id):
    """Calcula el pago mensual de cuotas para una tarjeta"""
    try:
        monthly_payment = CardInstallment.get_monthly_payment_for_card(card_id)
        return jsonify({'monthly_payment': monthly_payment}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para ver detalle de tarjeta
@main_bp.route('/cards/<card_id>')
def card_detail(card_id):
    """Página de detalle de una tarjeta"""
    return render_template('card_detail.html', card_id=card_id)

# API Endpoints - Cash
@main_bp.route('/api/cash', methods=['GET'])
def api_get_cash():
    """Obtiene todos los registros de efectivo"""
    try:
        cash_list = Cash.get_all()
        return jsonify(cash_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/cash', methods=['POST'])
def api_create_cash():
    """Crea un nuevo registro de efectivo"""
    try:
        data = request.get_json()
        cash_id = Cash.create(data)
        return jsonify({'id': cash_id, 'message': 'Efectivo registrado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/cash/<cash_id>', methods=['PUT'])
def api_update_cash(cash_id):
    """Actualiza un registro de efectivo"""
    try:
        data = request.get_json()
        Cash.update(cash_id, data)
        return jsonify({'message': 'Efectivo actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/cash/<cash_id>', methods=['DELETE'])
def api_delete_cash(cash_id):
    """Elimina un registro de efectivo"""
    try:
        Cash.delete(cash_id)
        return jsonify({'message': 'Efectivo eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Endpoints - Savings Goals
@main_bp.route('/api/goals', methods=['GET'])
def api_get_goals():
    """Obtiene todas las metas de ahorro"""
    try:
        goals = SavingsGoal.get_all()
        return jsonify(goals), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/goals', methods=['POST'])
def api_create_goal():
    """Crea una nueva meta de ahorro"""
    try:
        data = request.get_json()
        goal_id = SavingsGoal.create(data)
        return jsonify({'id': goal_id, 'message': 'Meta creada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/goals/<goal_id>', methods=['PUT'])
def api_update_goal(goal_id):
    """Actualiza una meta de ahorro"""
    try:
        data = request.get_json()
        SavingsGoal.update(goal_id, data)
        return jsonify({'message': 'Meta actualizada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/goals/<goal_id>', methods=['DELETE'])
def api_delete_goal(goal_id):
    """Elimina una meta de ahorro"""
    try:
        SavingsGoal.delete(goal_id)
        return jsonify({'message': 'Meta eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Endpoints - Loans
@main_bp.route('/api/loans', methods=['GET'])
def api_get_loans():
    """Obtiene todos los préstamos"""
    try:
        loans = Loan.get_all()
        return jsonify(loans), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/loans', methods=['POST'])
def api_create_loan():
    """Crea un nuevo préstamo"""
    try:
        data = request.get_json()
        loan_id = Loan.create(data)
        return jsonify({'id': loan_id, 'message': 'Préstamo creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/loans/<loan_id>', methods=['PUT'])
def api_update_loan(loan_id):
    """Actualiza un préstamo"""
    try:
        data = request.get_json()
        Loan.update(loan_id, data)
        return jsonify({'message': 'Préstamo actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/loans/<loan_id>', methods=['DELETE'])
def api_delete_loan(loan_id):
    """Elimina un préstamo"""
    try:
        Loan.delete(loan_id)
        return jsonify({'message': 'Préstamo eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Endpoints - Monthly Budget
@main_bp.route('/api/budget/current', methods=['GET'])
def api_get_current_budget():
    """Obtiene el presupuesto del mes actual"""
    try:
        budget = MonthlyBudget.get_current_budget()
        return jsonify(budget), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/budget/<budget_id>', methods=['PUT'])
def api_update_budget(budget_id):
    """Actualiza el presupuesto mensual"""
    try:
        data = request.get_json()
        MonthlyBudget.update_budget(budget_id, data)
        return jsonify({'message': 'Presupuesto actualizado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/budget/calculate', methods=['GET'])
def api_calculate_balance():
    """Calcula el balance mensual"""
    try:
        balance = MonthlyBudget.calculate_monthly_balance()
        return jsonify(balance), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Endpoints - Personal Loans
@main_bp.route('/api/personal-loans', methods=['GET'])
def api_get_personal_loans():
    """Obtiene todos los préstamos personales"""
    try:
        loans = PersonalLoan.get_all()
        return jsonify(loans), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/personal-loans/summary', methods=['GET'])
def api_get_personal_loans_summary():
    """Obtiene resumen de préstamos personales"""
    try:
        summary = PersonalLoan.get_summary()
        return jsonify(summary), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/personal-loans', methods=['POST'])
def api_create_personal_loan():
    """Crea un nuevo préstamo personal"""
    try:
        data = request.get_json()
        loan_id = PersonalLoan.create(data)
        return jsonify({'id': loan_id, 'message': 'Préstamo registrado'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/personal-loans/<loan_id>', methods=['PUT'])
def api_update_personal_loan(loan_id):
    """Actualiza un préstamo personal"""
    try:
        data = request.get_json()
        PersonalLoan.update(loan_id, data)
        return jsonify({'message': 'Préstamo actualizado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/personal-loans/<loan_id>', methods=['DELETE'])
def api_delete_personal_loan(loan_id):
    """Elimina un préstamo personal"""
    try:
        PersonalLoan.delete(loan_id)
        return jsonify({'message': 'Préstamo eliminado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

